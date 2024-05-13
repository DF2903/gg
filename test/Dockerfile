FROM python:3.10-alpine3.19

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /temp/requirements.txt
COPY app /app

RUN pip install -r /temp/requirements.txt

