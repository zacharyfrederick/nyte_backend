from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import action

from django.http import JsonResponse

from ..serializers import VenueSerializer, ReloadSerializer
from ..models import Venue
from ..models import Reload

class VenueViewset(viewsets.ModelViewSet):
    serializer_class = VenueSerializer
    queryset = Venue.objects.all()
