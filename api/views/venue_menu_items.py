from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import action

from django.http import JsonResponse

from ..serializers import MenuItemSerializer
from ..models import MenuItem

class VenueMenuItemViewset(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    
    def get_queryset(self):
        return MenuItem.objects.filter(venue=self.kwargs['venues_pk'])
