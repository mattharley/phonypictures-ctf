#!/bin/sh
cd /home/hero/Documents/phonypictures-ctf/ && gunicorn 'linkedout:app' -b 0.0.0.0:7000