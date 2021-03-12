# Dockerfile pour demonstration Docker n°1 - Application flask 


FROM debian:9

MAINTAINER Saadia Bayou

RUN apt-get update -y && apt-get install python -y\
    && apt-get install python-flask -y

COPY . /app

WORKDIR /app


CMD python script1.py
