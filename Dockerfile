FROM python:3.11

ADD requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /app
