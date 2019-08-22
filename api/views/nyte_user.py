from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import action
from rest_framework import status

from django.http import JsonResponse

from ..serializers import NyteUserSerializer, ReloadSerializer
from ..models import NyteUser
from ..models import Reload
from ..managers import FacebookManager

import stripe

class NyteUserViewset(viewsets.ModelViewSet):
    serializer_class = NyteUserSerializer
    queryset = NyteUser.objects.all()

    @action(detail=True, methods=['get'])
    def balance(self, request, *args, **kwargs):
        user = self.get_object()
        return Response({"balance": user.account_balance}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def ephemeral_key(self, request, **kwargs):
        try:
            user = self.get_object();
            api_version = request.data['api_version']
            key = stripe.EphemeralKey.create(customer=user.stripe_id, stripe_version=api_version)
            return Response({"key": key})
        except KeyError:
            return Response({"error": "data not provided"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["post"])
    def facebook_logout(self, request, **kwargs):
        try:
            user = self.get_object()
            access_token = request.data['access_token']
            fb = FacebookManager()
            request_resp = fb.send_request(access_token=access_token, logout=True)

            if request_resp is not None:
                return JsonResponse(request_resp, safe=False)
            else:
                return Response({"error": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except KeyError:
            return Response({"errpr": "access_token not provided"}, status=status.HTTP_400_BAD_REQUEST)

