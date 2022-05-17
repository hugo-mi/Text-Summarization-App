# STAGE 1 --------------------------------------------
FROM python:3.8-alpine as base
RUN apk update && apk add build-base

WORKDIR /src
COPY ./requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

COPY ./src /src


# STAGE 2 --------------------------------------------
FROM python:3.8-alpine

COPY --from=base /usr/local/lib/python3.8 /usr/local/lib/python3.8
COPY --from=base /usr/local/bin/gunicorn /usr/local/bin/gunicorn
COPY --from=base /src/ /src
WORKDIR /src


ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:80", "app:app"]