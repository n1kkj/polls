FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN apt update

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
WORKDIR /code/

EXPOSE 8000