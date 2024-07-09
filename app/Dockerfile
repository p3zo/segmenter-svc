# syntax = docker/dockerfile:1.0-experimental

FROM python:3.10-slim-buster as builder

## install dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        netcat-openbsd \
        gcc \
        git-all && \
    apt-get clean

FROM builder

SHELL ["/bin/bash", "-c"]

ENV APP_DIR=/opt/segmenter-svc

COPY requirements.txt $APP_DIR/requirements.txt
COPY deploy/tools $APP_DIR/deploy/tools/
COPY setup.py $APP_DIR/setup.py
COPY segmenter $APP_DIR/segmenter/

WORKDIR $APP_DIR

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m pip install -e .

EXPOSE 5000

ENTRYPOINT ["/bin/bash", "-c"]
