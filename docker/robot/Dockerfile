FROM python:3.6-alpine

ENV ROBOT_HOME /robot

RUN mkdir -p ${ROBOT_HOME}/conf/
#Install packages
# cryptography requires a lot of deps
RUN apk update
RUN apk add gcc g++ make build-base libffi-dev openssl-dev chromium chromium-chromedriver
RUN rm -rf /var/cache/apk/*

COPY conf/requirements.txt ${ROBOT_HOME}/conf/
RUN pip install --no-cache-dir -r ${ROBOT_HOME}/conf/requirements.txt

ENV SCRIPT_DIR=${ROBOT_HOME}/script \
    CONF_DIR=${ROBOT_HOME}/conf \
    PY_CMD='python3.6' \
    LOG_DIR=/var/log

CMD ["sh"]
