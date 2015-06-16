#!/bin/sh
sudo Xvfb :10 -ac &
export DISPLAY=:10
firefox &

cd /home/hero/Documents/phonypictures-ctf/ && python selenium.py