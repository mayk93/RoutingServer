#!/usr/bin/env bash

kill -9 $(cat /tmp/routing_server.pid)
rm /tmp/routing_server.pid