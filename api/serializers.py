from rest_framework import serializers
from . import models

class NyteUserSerializer(serializers.Serializer):
    class Meta:
        model = models.NyteUser
        fields = "__all__"

class VenueSerializer(serializers.Serializer):
    class Meta:
        model = models.Venue
        fields = "__all__"

class EventSerializer(serializers.Serializer):
    class Meta:
        model = models.Event
        fields = "__all__"
    
class SpecialSerializer(serializers.Serializer):
    class Meta:
        model = models.Special
        fields = "__all__"

class AccountSerializer(serializers.Serializer):
    class Meta:
        model = models.Account
        fields = "__all__"

class AccountInformationSerializer(serializers.Serializer):
    class Meta:
        model = models.AccountInformation
        fields = "__all__"

class IdentitySerializer(serializers.Serializer):
    class Meta:
        model = models.Identity
        fields = "__all__"

class MenuItemSerializer(serializers.Serializer):
    class Meta:
        model = models.MenuItem
        fields = "__all__"

class TransactionSerializer(serializers.Serializer):
    class Meta:
        model = models.Transaction
        fields = "__all__"

class WorksAtSerializer(serializers.Serializer):
    class Meta:
        model = models.WorksAt
        fields = "__all__"

class UserSessionSerializer(serializers.Serializer):
    class Meta:
        model = models.UserSession
        fields = "__all__"