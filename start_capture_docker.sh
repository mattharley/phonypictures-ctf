#!/bin/sh
docker run -p 172.17.42.1:5001:5001 -t phony/intranet ./start_capture.sh
