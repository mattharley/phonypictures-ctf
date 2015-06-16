#!/bin/sh
docker run -p 5000:5000 -a stdin -a stdout -i -t phony/intranet ./start_intranet.sh