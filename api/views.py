from . import serializers
from . import models
from rest_framework import generics

class NyteUserList(generics.ListCreateAPIView):
    queryset = models.NyteUser.objects.all()
    serializer_class = serializers.NyteUserSerializer

class NyteUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.NyteUser.objects.all()
    serializer_class = serializers.NyteUserSerializer

class AccountList(generics.ListCreateAPIView):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer

class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer

class AccountInformationList(generics.ListCreateAPIView):
    queryset = models.AccountInformation.objects.all()
    serializer_class = serializers.AccountInformationSerializer

class AccountInformationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AccountInformation.objects.all()
    serializer_class = serializers.AccountInformationSerializer

class EventList(generics.ListCreateAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

class IdentityList(generics.ListCreateAPIView):
    queryset = models.Identity.objects.all()
    serializer_class = serializers.IdentitySerializer

class IdentityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Identity.objects.all()
    serializer_class = serializers.IdentitySerializer

class MenuItemList(generics.ListCreateAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer

class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer

class SpecialList(generics.ListCreateAPIView):
    queryset = models.Special.objects.all()
    serializer_class = serializers.SpecialSerializer

class SpecialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Special.objects.all()
    serializer_class = serializers.SpecialSerializer

class TransactionList(generics.ListCreateAPIView):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer

class UserSessionList(generics.ListCreateAPIView):
    queryset = models.UserSession.objects.all()
    serializer_class = serializers.UserSessionSerializer

class UserSessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.UserSession.objects.all()
    serializer_class = serializers.UserSessionSerializer

class VenueList(generics.ListCreateAPIView):
    queryset = models.Venue.objects.all()
    serializer_class = serializers.VenueSerializer

class VenueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Venue.objects.all()
    serializer_class = serializers.VenueSerializer

class WorksAtList(generics.ListCreateAPIView):
    queryset = models.WorksAt.objects.all()
    serializer_class = serializers.WorksAtSerializer

class WorksAtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.WorksAt.objects.all()
    serializer_class = serializers.WorksAtSerializer






