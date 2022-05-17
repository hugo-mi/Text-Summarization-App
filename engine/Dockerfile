# STAGE 1 --------------------------------------------
FROM python:3.8-buster as base

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# STAGE 2 --------------------------------------------
FROM python:3.8-buster

COPY --from=base /usr/local/lib/python3.8 /usr/local/lib/python3.8
COPY --from=base /usr/local/bin/gunicorn /usr/local/bin/gunicorn
COPY ./src/ /src
WORKDIR /src


ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:80", "--timeout", "720", "app:app"]