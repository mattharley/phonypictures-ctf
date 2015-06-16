#!/bin/sh
docker run -p 5001:5001 -a stdin -a stdout -i -t phony/intranet ./start_capture.sh