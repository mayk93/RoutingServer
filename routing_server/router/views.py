import logging
import requests
from rest_framework import status
from django.http import HttpResponse
from django.conf import settings

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


def api(request):
    response = {}

    route_path = request.path[len("/api/"):]
    url = build_url(route_path)
    response_status = status.HTTP_200_OK

    if url:
        try:
            response = requests.get(url, stream=True)
        except Exception as e:
            print(e)
            logging.exception(e)
            response_status = status.HTTP_400_BAD_REQUEST

    return HttpResponse(
        response, content_type=response.headers.get('content-type', 'application/json'), status=response_status
    )
