from rest_framework import serializers
from . import models

class NyteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NyteUser
        exclude = ("password",)

class NyteUserStrippedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NyteUser
        fields = ("id", "first_name", "last_name", "id_image")

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

class TransactionSerializer(serializers.ModelSerializer):
    venue_name = serializers.SerializerMethodField()
    user_data = serializers.SerializerMethodField()

    class Meta:
        model = models.Transaction
        fields = "__all__"

    def get_venue_name(self, obj):
        return obj.venue.name 

    def get_user_data(self, obj):
        print(obj.user.id_image)
        return {"first_name": obj.user.first_name, "last_name": obj.user.last_name}
        
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

class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Verification
        fields = "__all__"

class VerificationIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VerificationID
        fields = "__all__"

class ReloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reload
        fields = "__all__"

class ViewBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NyteUser
        fields = ("id", "stripe_id", "account_balance", )

class ValueStrippedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OptionValue
        fields = ("id",)

class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OptionValue
        fields = "__all__"


class OptionStrippedSerializer(serializers.ModelSerializer):
    values = ValueStrippedSerializer(many=True)

    class Meta:
        model = models.MenuOption
        fields = ('id', 'values')

class OptionSerializer(serializers.ModelSerializer):
    values = ValueSerializer(many=True)

    class Meta:
        model = models.MenuOption
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    #options = OptionStrippedSerializer(many=True)

    class Meta:
        model = models.Category
        fields = "__all__"


class OptionPairingSerializer(serializers.ModelSerializer):
    option = OptionStrippedSerializer()

    class Meta:
        model = models.OptionPairing
        fields = ("option",)

class MenuItemSerializer(serializers.ModelSerializer):
    pairings = OptionPairingSerializer(many=True)
    
    class Meta:
        model = models.MenuItem
        fields = "__all__"
