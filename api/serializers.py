from rest_framework import serializers
from . import models

class NyteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NyteUser
        fields = "__all__"

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Venue
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = "__all__"
    
class SpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Special
        fields = "__all__"

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = "__all__"

class AccountInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AccountInformation
        fields = "__all__"

class IdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Identity
        fields = "__all__"

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MenuItem
        fields = "__all__"

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = "__all__"

class WorksAtSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorksAt
        fields = "__all__"

class UserSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserSession
        fields = "__all__"

class ProtoMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProtoMenuItem
        fields = "__all__"

class ProtoOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProtoOrder
        fields = "__all__"