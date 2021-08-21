FROM python:3.9.6-alpine


ENV PYTHONBUFFERED 1

RUN apk update \
  && apk add postgresql-dev gcc python3-dev musl-dev build-base py-pip libffi-dev openssl-dev jpeg-dev zlib-dev


RUN pip install --upgrade pip \
  && pip install --upgrade setuptools \
  && pip install --upgrade pipenv  

COPY ./requirements.txt /requirements.txt
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
RUN pip install cryptography
RUN pip install -r /requirements.txt

RUN mkdir /usr/notes
WORKDIR /usr/notes

COPY . .

CMD ["sh", "-c", "python manage.py collectstatic --no-input; python manage.py migrate; python manage.py runserver 0.0.0.0:8000 --noreload"]