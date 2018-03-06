#!/usr/bin/env bash

touch /tmp/routing_server.pid

export PROD="true"

uwsgi --chmod-socket=666 --uwsgi-socket /home/deploy/other_config/routing_server/routing_server.sock --wsgi-file /home/deploy/other_data/RoutingServer/routing_server/routing_server/wsgi.py

echo $! > /tmp/routing_server.pid