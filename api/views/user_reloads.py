from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import action

from ..serializers import NyteUserSerializer, ReloadSerializer
from ..models import NyteUser
from ..models import Reload

class UserReloadsViewset(viewsets.ModelViewSet):
    serializer_class = ReloadSerializer
    
    def get_queryset(self):
        return Reload.objects.filter(user=self.kwargs['users_pk'])
