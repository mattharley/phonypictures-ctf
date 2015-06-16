#!/bin/sh
cd /home/hero/Documents/phonypictures-ctf/ && gunicorn 'amazone:app' -b 0.0.0.0:8000