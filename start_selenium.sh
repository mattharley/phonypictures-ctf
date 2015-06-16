#!/bin/sh
sudo Xvfb :10 -ac
export DISPLAY=:10
firefox &

python selenium.py