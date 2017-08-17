FROM python:3.5.3

ADD . /gateway
WORKDIR /gateway

RUN chmod +x /gateway/run.sh

RUN apt-get update && apt-get install -y \
  netcat

RUN /bin/bash -c "pip3 install -r /gateway/requirements/base.txt"
