# Get python
FROM python:3.8.6

ENV PYTHONUNBUFFERED 1

#Container
RUN mkdir /code
WORKDIR /code

RUN pip install pip -U
ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/