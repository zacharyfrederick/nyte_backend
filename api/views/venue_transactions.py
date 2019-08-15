from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import action
from rest_framework.exceptions import APIException

from django.http import JsonResponse

from ..serializers import TransactionSerializer
from ..models import Transaction

class VenueTransactionsViewsets(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    
    def get_queryset(self):
        venue = self.kwargs.get('venues_pk')
        return Transaction.objects.filter(venue=venue)
