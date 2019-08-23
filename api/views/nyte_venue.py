from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import action
from rest_framework.decorators import action

from fcm_django.models import FCMDevice

from django.http import JsonResponse

from ..serializers import VenueSerializer, ReloadSerializer
from ..models import Venue
from ..models import Reload
from ..models import BartenderDevice

class VenueViewset(viewsets.ModelViewSet):
    serializer_class = VenueSerializer
    queryset = Venue.objects.all()

    @action(detail=True, methods=['post'])
    def register_device(self, request, **kwargs):
        try:
            venue = self.get_object()
            token = request.data['fcm_token']
            device = FCMDevice.objects.create(registration_id=token)
            bar_device = BartenderDevice.objects.create(device=device, venue=venue)
            return Response({"status": "success"})
        except KeyError:
            return Response({"error":"fcm_token not provided"})
            



