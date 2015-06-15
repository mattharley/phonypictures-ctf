FROM python:2-onbuild
MAINTAINER Matt Harley <matt@mattharley.com>
RUN mkdir -p /usr/src/app/static
RUN mkdir -p /usr/src/app/templates
ONBUILD COPY ../static/* /usr/src/app/static
ONBUILD COPY ../templates/* /usr/src/app/templates
CMD [ "gunicorn", "-b 0.0.0.0:8000", "linkedout:app" ]