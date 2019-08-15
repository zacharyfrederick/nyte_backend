from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import action

from django.http import JsonResponse

from ..serializers import NyteUserSerializer, ReloadSerializer
from ..models import NyteUser
from ..models import Reload

class NyteUserViewset(viewsets.ModelViewSet):
    serializer_class = NyteUserSerializer
    queryset = NyteUser.objects.all()

    @action(detail=True, renderer_classes=[StaticHTMLRenderer])
    def balance(self, request, *args, **kwargs):
        user = self.get_object()
        return JsonResponse({"balance": user.account_balance})
