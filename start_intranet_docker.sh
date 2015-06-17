#!/bin/sh
docker run -p 172.17.42.1:5000:5000 -p 172.17.42.1:2222:22 -t phony/intranet ./start_intranet.sh
