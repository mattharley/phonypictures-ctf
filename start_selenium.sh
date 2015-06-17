#!/bin/sh
Xvfb :10 -ac &
export DISPLAY=:10

#cd /home/hero/Documents/phonypictures-ctf/ && python run_selenium.py
