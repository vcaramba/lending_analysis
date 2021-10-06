FROM python:3.8-slim-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app/

RUN apt-get update \
    && apt-get clean \
    && apt-get update -qqq \
    && pip3 install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app

CMD python3 -m notebook --port=8888 --no-browser --ip=0.0.0.0 --allow-root