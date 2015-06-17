#!/bin/sh
docker run -p 172.17.42.1:5002:22 -t phony/intranet ./start_ssh.sh
