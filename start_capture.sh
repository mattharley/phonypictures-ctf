#!/bin/sh
gunicorn 'capture:app' -b 0.0.0.0:7000