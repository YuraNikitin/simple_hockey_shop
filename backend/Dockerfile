FROM python:3.8-slim AS base

ENV TZ Europe/Moscow

ENV PYTHONDONTWRITEBYTECODE yes
ENV PYTHONPATH=/usr/src/app

WORKDIR $PYTHONPATH

RUN apt-get update -y && \
    apt-get install -y lynx && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

