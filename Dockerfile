FROM python:3.5.3
ADD requirements /service/requirements
ADD service /service/service

COPY config/config.yml /service/config/config.yml
COPY rpc /service/rpc
COPY run.sh /service
COPY run_rpc.sh /service
WORKDIR /service

RUN chmod +x /service/run.sh
RUN chmod +x /service/run_rpc.sh

RUN apt-get update && apt-get install -y \
  netcat

RUN /bin/bash -c "pip3 install -r /service/requirements/base.txt"


#CMD /service/run.sh
#CMD ["nameko","run" "/service/rpc/service_hello"]
