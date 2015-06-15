FROM python:2-onbuild
MAINTAINER Matt Harley <matt@mattharley.com>


CMD [ "gunicorn", "-b 0.0.0.0:8000", "linkedout:app" ]