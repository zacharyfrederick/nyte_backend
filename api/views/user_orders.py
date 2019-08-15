from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import action

from ..serializers import NyteUserSerializer, TransactionSerializer
from ..models import NyteUser
from ..models import Transaction

class UserOrdersViewset(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    
    def get_queryset(self):
        return Transaction.objects.filter(user=self.kwargs['users_pk'])
