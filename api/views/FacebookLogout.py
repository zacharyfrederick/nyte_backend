from .. import models
from rest_framework.response import Response
from rest_framework.views import APIView
import stripe
from ..managers import FacebookManager
import json
from django.http import JsonResponse

class FacebookLogout(APIView):
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            try:
                access_token = json.loads(request.body)['access_token']
                fb_manager = FacebookManager()
                request_resp = fb_manager.send_request(access_token=access_token, logout=True)
                if request_resp is not None:
                    return JsonResponse(request_resp, safe=False)
                else:
                    return JsonResponse({"error": "an error occurred"})
            except KeyError:
                return JsonResponse({"error": "no access_token supplied"})
        else:
            return JsonResponse({"error": "only POST allowed to this url"})