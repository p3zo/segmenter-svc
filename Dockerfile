# syntax = docker/dockerfile:1.0-experimental

FROM python:3.10-slim-buster as builder

## install dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        netcat-openbsd \
        gcc \
        git-all \
        p7zip-full && \
    apt-get clean

FROM builder

SHELL ["/bin/bash", "-c"]

ENV APP_DIR=/opt/segmenter-svc

COPY app/ $APP_DIR/
COPY aws_lambda $APP_DIR/aws_lambda/

WORKDIR $APP_DIR

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m pip install -e .

EXPOSE 5000

ENTRYPOINT ["/bin/bash", "-c"]
