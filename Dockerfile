FROM python:3.6-alpine
MAINTAINER Erignoux Laurent <lerignoux@gmail.com>

RUN apk update && apk add gcc musl-dev

ADD . /app
RUN cd app && pip3 install -r requirements.txt
WORKDIR /app

CMD python3 /app/app.py
