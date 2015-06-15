FROM python:2-onbuild
MAINTAINER Matt Harley <matt@mattharley.com>

RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/static
RUN mkdir -p /usr/src/app/templates

ONBUILD COPY ../static/* /usr/src/app/static
ONBUILD COPY ../templates/* /usr/src/app/templates
ONBUILD COPY ../linkedout.py /usr/src/app/
ONBUILD COPY ../requirements.txt /usr/src/app/

ONBUILD RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app
CMD [ "gunicorn", "-b 0.0.0.0:8000", "linkedout:app" ]