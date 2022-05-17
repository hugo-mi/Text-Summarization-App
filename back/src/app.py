# app.py
import os
import logging
import time
import re
from flask import Flask, json, jsonify, abort, request, redirect
import requests
import logging
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from rev_ai import apiclient
import time
import asyncio
import threading
from datetime import datetime, timedelta

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

ENGINE_URL = "http://engine"

app = Flask(__name__)

uri = "mongodb://{}:27017/aubaysum".format(
    os.environ["ME_CONFIG_MONGODB_SERVER"])
app.logger.info(f"Database URI : {uri}")

app.config["MONGO_URI"] = uri

mongo = PyMongo(app)
app.logger.info(mongo.cx)

# REV AI api key init
client = apiclient.RevAiAPIClient(os.environ['REV_AI_KEY'])


@app.route('/api/test')
def test_endpoint():
    return 'alright'


@app.route('/api/testengine')
def test_engine():
    app.logger.info("Test request received")
    response = requests.post(ENGINE_URL + "/testengine",
                             data={"payload": "test payload"}).text
    return f"Engine said : {response}"


@app.route('/api/summary/<string:summary_id>')
def get_summary(summary_id):
    # show the summary with the given id, the id is an integer

    # retreive summary from database
    summary = mongo.db.summaries.find_one({"_id": ObjectId(summary_id)})
    if summary is not None:
        summary["id"] = str(summary["_id"])
        summary.pop("_id")
        #app.logger.info(type(summary))
        #app.logger.info(summary)

        # make the response
        response = jsonify(summary)
        return response
    else:
        abort(404)

@app.route('/api/summary/<string:summary_id>/update', methods = ['POST'])
def update_summary(summary_id):
    base = mongo.db.summaries.find_one({"_id":ObjectId(summary_id)})
    data = request.json
    data["transcript"] = base["transcript"]
    ack = mongo.db.summaries.update_one({"_id":ObjectId(summary_id)}, {"$set" : data})

    if not ack:
        abort(500)
    else:
        return '', 204 # no response

def insert_cr_into_db(payload):
    nb_summaries = mongo.db.summaries.count_documents({})
    payload["id"] = nb_summaries
    result = mongo.db.summaries.insert_one(payload)

    if not result.acknowledged:
        abort(500)
    else:
        return str(result.inserted_id)

def update_cr_db(id, json_file):
    ack = mongo.db.summaries.update_one({"_id":ObjectId(id)}, json_file).acknowledged
    if not ack:
        abort(500)
    else:
        return True

def get_ai_summary(text):
    response = requests.post(f"{ENGINE_URL}/summarize",
                             json={"text": text}
                             )

    ai_result = json.loads(response.text)
    return ai_result

def create_cr_text_ai_thread(text, id):
    ai_result = get_ai_summary(text)
    ack_update = update_cr_db(id, {"$set" : {"summary" : ai_result, "status" : "done"}})



@app.route("/api/createCR/text", methods=['POST'])
def create_cr_text():
    app.logger.info("Received new CR request")

    # receiving json data
    payload_json = request.json

    payload_json['status'] = 'in_progress'
    id = insert_cr_into_db(payload_json)

    # Second thread to transcribe
    t = threading.Thread(target=create_cr_text_ai_thread, args=(payload_json['transcript'], id))
    t.start()

    return jsonify({"id" : id})


def await_revai_transcript(job_id):

    job_details = client.get_job_details(job_id)
    job_status = job_details.status.name

    app.logger.info(
        f"Waiting for Rev AI to transcribe ... ")
    while (job_status == "IN_PROGRESS"):
        app.logger.info(f"Rev AI is transcribing : {job_status}")
        time.sleep(10)
        job_status = client.get_job_details(job_id).status.name
    app.logger.info(f"Rev AI has finished transcribing ")

    return client.get_transcript_text(job_id)


def clean_transcript(transcript):

    lines = transcript.split('\n')
    cleaned_transcript = ''
    for line in lines : 
        cleaned_transcript += line[24:]
    return cleaned_transcript


def audio_to_summary(audio, id):

    # ------------
    # Multi-part/form-data requests to the /jobs endpoint have a concurrency limit of 10 and a file size limit of 2GB
    # ------------

    # Submitting transcription job to Rev AI
    job = client.submit_job_local_file(
        audio, metadata=None,
        callback_url=None,
        skip_diarization=False,
        language="fr",
        custom_vocabularies=None)
    job_details = client.get_job_details(job.id)
    app.logger.info(f"Audio sent to Rev AI, job details : {job_details} ")

    # Retrieving Transcript
    transcribed_text = await_revai_transcript(job.id)
    app.logger.info(f"Transcribed text from Rev AI : {transcribed_text}")

    # Cleaning Transcript
    transcribed_text = clean_transcript(transcribed_text)
    app.logger.info(f"Cleaned Transcript : {transcribed_text}")

    # send to engine to process data into summary
    ai_result = get_ai_summary(transcribed_text)

    # update in database
    ack_update = update_cr_db(id, {"$set" : {"transcript": transcribed_text, "summary" : ai_result, "status" : "done"}})



@app.route("/api/createCR/audio", methods=['POST'])
def submit_cr_audio():
    # send a form with json in teh data field and the file in the file field
    app.logger.info("Received new audio CR request")

# receiving json data
    payload_json = json.loads(request.form.get("data"))
    #app.logger.info(payload_json)
    payload_audio_file = request.files["file"]
    #app.logger.info(payload_audio_file)  # see werkzeug.FileStorage online

    # receiving audio data

    #app.logger.info(f'Received audio file : {payload_audio_file}')

    # Temporarily saving the file
    payload_audio_file.save("/tmp/audio")
    payload_audio_file.close()

    # Main thread to record the pending request
    payload_json['status'] = 'in_progress'
    id = insert_cr_into_db(payload_json)

    # Second thread to transcribe
    t = threading.Thread(target=audio_to_summary, args=("/tmp/audio", id))
    t.start()

    return {"id": id}, 200


@app.route("/api/summaries/list")
def list_summaries():
    results = list(mongo.db.summaries.find(filter={}, projection=[
        "_id", "title", "attendees", "date", "projectGroup", "generatorName", "status"]))
    results_final = []
    for result in results:
        result["id"] = str(result["_id"])
        result.pop("_id")
        results_final.append(result)
    app.logger.info(results)
    return jsonify(results)


@app.route('/api/summary/ext/<string:summary_id>', methods=['POST'])
def reset_summary_ext(summary_id):
    # reset the extractive part of the summary by deleting entire user modifications 

    now = datetime.now() + timedelta(hours=2)
    current_date = now.strftime("%d/%m/%Y")
    current_hour = now.strftime("%H:%M:%S")
    current_date_format = current_date + " à " + current_hour
    ack = mongo.db.summaries.update_one({"_id" : ObjectId(summary_id)}, {"$set" : {"summary.extractive.lastUpdate": current_date_format}, "$unset" : {"summary.extractive.edited":"", "summary.extractive.html":""}}).acknowledged

    if not ack:
        app.logger.log("Error update")
        abort(500)

    return "", 201

@app.route('/api/summary/abs/<string:summary_id>', methods=['POST'])
def reset_summary_abs(summary_id):
    # reset the extractive part of the summary by deleting entire user modifications 

    now = datetime.now() + timedelta(hours=2)
    current_date = now.strftime("%d/%m/%Y")
    current_hour = now.strftime("%H:%M:%S")
    current_date_format = current_date + " à " + current_hour
    ack = mongo.db.summaries.update_one({"_id" : ObjectId(summary_id)}, {"$set" : {"summary.abstractive.lastUpdate": current_date_format}, "$unset" : {"summary.abstractive.edited":"", "summary.abstractive.html":""}}).acknowledged

    if not ack:
        app.logger.log("Error update")
        abort(500)

    return "", 201

@app.route('/api/summary/<string:summary_id>/delete', methods=["GET"])
def delete_summary(summary_id):
    ack = mongo.db.summaries.delete_one({"_id" : ObjectId(summary_id)})

    if not ack:
        abort(500)
    else:
        return "", 201

@app.route('/api/summaries/search', methods=["POST"])
def search_summary():
    research = request.json['research']
    margin = request.json["margin"]
    results = list(mongo.db.summaries.find(filter={ "$text": { "$search": f"\"{research}\"" } }, projection=[
        "_id", "title", "date", "projectGroup", "summary"]))
    results_final = []
    regex = re.compile(research, re.IGNORECASE)
    for result in results:
        matches = {}
        result["id"] = str(result["_id"])
        result.pop("_id")

        for method in result["summary"]:
            matches[method] = {}
            for style in result["summary"][method]:
                if style != "html":
                    text = result["summary"][method][style]
                    search = re.search(regex, text)
                    if search is not None:
                        matches[method][style] = {}
                        start = search.start()
                        end = search.end()
                        matches[method][style]["extract"] = result["summary"][method][style][max(0, start-margin):min(end+margin, len(text))]
                        search = re.search(regex, matches[method][style]["extract"])
                        matches[method][style]["start"] = search.start()
                        matches[method][style]["end"] = search.end()
            if matches[method] =={}:
                matches.pop(method)
        result["matches"] = matches
        result.pop("summary")

        results_final.append(result)
    return jsonify(results)
    
