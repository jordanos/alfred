FROM python:3.10-slim-buster

RUN apt update
RUN apt install -y libpq-dev cron g++ build-essential

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN mkdir cs-api
WORKDIR /cs-api

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /cs-api