FROM python:3.10.10-bullseye
WORKDIR /bot

RUN apk --update add \
    curl \
    gcc \
    musl-dev \
    linux-headers \
    build-base \
    libffi-dev \
    bash

COPY requirements.txt /bot/
RUN pip install -r requirements.txt
COPY . /bot
CMD python app.py