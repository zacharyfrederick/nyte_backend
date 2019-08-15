from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import action
from rest_framework.exceptions import APIException

from django.http import JsonResponse

from ..serializers import OptionSerializer
from ..models import MenuOption, OptionPairing

class VenueOptionsViewset(viewsets.ModelViewSet):
    serializer_class = OptionSerializer
    
    def get_queryset(self):
        queryset = set()
        try:
            venue = int(self.kwargs['venues_pk'])
        except ValueError:
            raise APIException("invalid venue id")
        
        for pairing in OptionPairing.objects.all():
            if venue is pairing.menu_item.venue.id:
                queryset.add(pairing.option.id)
            
        return MenuOption.objects.filter(pk__in=queryset)
