FROM python:3.10-alpine
RUN apk update && apk add gcc
RUN pip3 install --upgrade pip
RUN mkdir /app
ADD . /app
WORKDIR /app
# TODO: Use requirements.txt
RUN pip3 install -r requirements.txt
