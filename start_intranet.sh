#!/bin/sh
gunicorn 'intranet:app' -b 0.0.0.0:6000