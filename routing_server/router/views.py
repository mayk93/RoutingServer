import logging
import json
import requests
from rest_framework import status
from django.http import HttpResponse
from django.conf import settings
from rest_framework.decorators import api_view

logging.basicConfig(level=logging.INFO)
servers = settings.SERVERS


def build_url(route_path):
    port = servers.get(route_path)
    if port is None:
        desired_server = route_path[:route_path[1:].find("/") + 1]
        port = servers.get(desired_server)
    if "/" in route_path:
        route_path = "/".join(route_path.split("/")[1:])

    return "http://localhost:%s/%s" % (port, route_path) if port else None


@api_view(['GET', 'POST', 'OPTIONS'])
def api(request):
    response = {}

    route_path = request.path[len("/api/"):]
    url = build_url(route_path)
    response_status = status.HTTP_200_OK

    if url:
        try:
            if request.method == "GET":
                response = requests.get(url, stream=True)
            elif request.method == "POST":
                response = requests.post(url, json=json.loads(request.body), stream=True)
            elif request.method == "OPTIONS":
                _response = HttpResponse()
                _response["Access-Control-Allow-Origin"] = "*"
                _response["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
                _response["Access-Control-Allow-Headers"] = "Content-Type,Accept"

                return _response
        except Exception as e:
            logging.exception(e)
            response_status = status.HTTP_400_BAD_REQUEST

    content_type = 'application/json' if isinstance(response, dict) else response.headers.get(
        'content-type', 'application/json'
    )

    _response = HttpResponse(
        response, content_type=content_type, status=response_status
    )
    _response["Access-Control-Allow-Origin"] = "*"
    _response["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
    _response["Access-Control-Allow-Headers"] = "Content-Type,Accept"

    return _response
