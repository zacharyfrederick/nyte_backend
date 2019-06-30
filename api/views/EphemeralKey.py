import json
from .. import models
from rest_framework.response import Response
from rest_framework.views import APIView
import stripe

class EphemeralKeyView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            user_id = json.loads(request.body)['user']
            api_version = json.loads(request.body)['api_version']
            try:
                user = models.NyteUser.objects.get(id=user_id)
                key = stripe.EphemeralKey.create(customer=user.stripe_id, stripe_version=api_version)
                return Response({"key": key})
            except models.NyteUser.DoesNotExist:
                return Response({"error": "Invalid user_id"})
        except KeyError as e:
            print(e)
            return Response({"error": "invalid credentials supplied"})