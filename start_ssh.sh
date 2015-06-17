#!/bin/sh
docker run -a stdin -a stdout -i -p 172.17.42.1:5002:22 -t phony/intranet '/etc/init.d/ssh start && cat'
