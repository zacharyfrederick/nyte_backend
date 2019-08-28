from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import action

from django.http import JsonResponse

from ..serializers import VenueImageSerializer
from ..models import VenueImage

class VenueImagesViewset(viewsets.ModelViewSet):
    serializer_class = VenueImageSerializer
    
    def get_queryset(self):
        return VenueImage.objects.filter(venue=self.kwargs['venues_pk'])
