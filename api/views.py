from . import serializers
from . import models
from rest_framework import generics

class NyteUserList(generics.ListCreateAPIView):
    queryset = models.NyteUser.objects.all()
    serializerClass = serializers.NyteUserSerializer

class NyteUserDetail(generics.CreateAPIView):
    queryset = models.NyteUser.objects.all()
    serializerClass = serializers.NyteUserSerializer

class AccountList(generics.ListCreateAPIView):
    queryset = models.Account.objects.all()
    serializerClass = serializers.AccountSerializer

class AccountDetail(generics.CreateAPIView):
    queryset = models.Account.objects.all()
    serializerClass = serializers.AccountSerializer

class AccountInformationList(generics.ListCreateAPIView):
    queryset = models.AccountInformation.objects.all()
    serializerClass = serializers.AccountInformationSerializer

class AccountInformationDetail(generics.CreateAPIView):
    queryset = models.AccountInformation.objects.all()
    serializerClass = serializers.AccountInformationSerializer

class EventList(generics.ListCreateAPIView):
    queryset = models.Event.objects.all()
    serializerClass = serializers.EventSerializer

class EventDetail(generics.CreateAPIView):
    queryset = models.Event.objects.all()
    serializerClass = serializers.EventSerializer

class IdentityList(generics.ListCreateAPIView):
    queryset = models.Identity.objects.all()
    serializerClass = serializers.IdentitySerializer

class IdentityDetail(generics.CreateAPIView):
    queryset = models.Identity.objects.all()
    serializerClass = serializers.IdentitySerializer

class MenuItemList(generics.ListCreateAPIView):
    queryset = models.MenuItem.objects.all()
    serializerClass = serializers.MenuItemSerializer

class MenuItemDetail(generics.CreateAPIView):
    queryset = models.MenuItem.objects.all()
    serializerClass = serializers.MenuItemSerializer

class SpecialList(generics.ListCreateAPIView):
    queryset = models.Special.objects.all()
    serializerClass = serializers.SpecialSerializer

class SpecialDetail(generics.CreateAPIView):
    queryset = models.Special.objects.all()
    serializerClass = serializers.SpecialSerializer

class TransactionList(generics.ListCreateAPIView):
    queryset = models.Transaction.objects.all()
    serializerClass = serializers.TransactionSerializer

class TransactionDetail(generics.CreateAPIView):
    queryset = models.Transaction.objects.all()
    serializerClass = serializers.TransactionSerializer

class UserSessionList(generics.ListCreateAPIView):
    queryset = models.UserSession.objects.all()
    serializerClass = serializers.UserSessionSerializer

class UserSessionDetail(generics.CreateAPIView):
    queryset = models.UserSession.objects.all()
    serializerClass = serializers.UserSessionSerializer

class VenueList(generics.ListCreateAPIView):
    queryset = models.Venue.objects.all()
    serializerClass = serializers.VenueSerializer

class VenueDetail(generics.CreateAPIView):
    queryset = models.Venue.objects.all()
    serializerClass = serializers.VenueSerializer

class WorksAtList(generics.ListCreateAPIView):
    queryset = models.WorksAt.objects.all()
    serializerClass = serializers.WorksAtSerializer

class WorksAtDetail(generics.CreateAPIView):
    queryset = models.WorksAt.objects.all()
    serializerClass = serializers.WorksAtSerializer






