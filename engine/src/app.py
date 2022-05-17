# app.py
from flask import Flask, request, jsonify
import json
import logging 
from models.camembert import Camembert
from models.mbarthez import MBARThez

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

camembert_model = Camembert()
app.logger.info("Camembert Model loaded")
mbarthez_model = MBARThez()
app.logger.info("mBARThez Model loaded")




@app.route('/testengine', methods=["POST"])
def test_ai():
    payload = request.json
    app.logger.info("Request received")
    return f"Engine received payload : {payload['payload']}"

@app.route('/summarize', methods=['POST'])
def summarize_endpoint():
    payload = request.json
    
    #app.logger.info(f"Job received {payload['text']}")
    #ai processing
    mbarthez_summary = mbarthez_model.summarize(payload["text"])
    camembert_summary = camembert_model.summarize(payload["text"])

    result = {
        "extractive" : {"raw":camembert_summary},
        "abstractive" : {"raw" :mbarthez_summary},
    }

    return json.dumps(result, ensure_ascii=False), 200