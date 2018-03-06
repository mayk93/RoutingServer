#!/usr/bin/env bash

touch /tmp/routing_server.pid

export PROD="true"

uwsgi --chmod-socket=666 --uwsgi-socket /home/deploy/routing_server/routing_server.sock --wsgi-file /home/deploy/RoutingServer/routing_server/routing_server/wsgi.py

echo $! > /tmp/routing_server.pid