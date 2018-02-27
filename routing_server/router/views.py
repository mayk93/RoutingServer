import logging
import requests
from rest_framework import status
from django.http import JsonResponse

logging.basicConfig(level=logging.INFO)


def api(request):
    try:
        desired_server = request.path[len("/api/"):]
        raise Exception("Going to server %s" % desired_server)
        response = requests.get(url, stream=True)
        response_status = status.HTTP_200_OK
    except Exception as e:
        logging.exception(e)
        response_status = status.HTTP_400_BAD_REQUEST

    return JsonResponse(
        {}, content_type='image/jpg', status=response_status
    )
