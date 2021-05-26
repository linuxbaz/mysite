FROM python:3.8.0b4-alpine3.10

WORKDIR /home/majid/app

ADD . /home/majid/app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD . /home/majid/app


