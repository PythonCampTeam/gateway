FROM python:3.5.3
ADD requirements /gateway/requirements
ADD service /gateway/service
ADD config /gateway/config
ADD integration /gateway/integration
#ARG PY_ENV

COPY run.sh /gateway
COPY run_rpc.sh /gateway
COPY __init__.py /gateway
WORKDIR /gateway

RUN chmod +x /gateway/run.sh
RUN chmod +x /gateway/run_rpc.sh

RUN apt-get update && apt-get install -y \
  netcat

RUN /bin/bash -c "pip3 install -r /gateway/requirements/base.txt"
