#DRF imports
from rest_framework import generics
from rest_framework.parsers import FileUploadParser
#Nyte imports
from .. import models
from .. import serializers

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

class TransactionByUser(generics.ListCreateAPIView):
    serializer_class = serializers.TransactionSerializer

    def get_queryset(self):
        return models.Transaction.objects.filter(user=self.kwargs['pk'])

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

class ProtoMenuItemList(generics.ListCreateAPIView):
    queryset = models.ProtoMenuItem.objects.all()
    serializer_class = serializers.ProtoMenuItemSerializer

class ProtoMenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProtoMenuItem.objects.all()
    serializer_class = serializers.ProtoMenuItemSerializer

class ProtoOrderList(generics.ListCreateAPIView):
    queryset = models.ProtoOrder.objects.all()
    serializer_class = serializers.ProtoOrderSerializer

class ProtoOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProtoOrder.objects.all()
    serializer_class = serializers.ProtoOrderSerializer

class VerificationCreation(generics.ListCreateAPIView):
    parser_class = (FileUploadParser,)
    queryset = models.Verification.objects.all()
    serializer_class = serializers.VerificationSerializer

class VerificationUpdate(generics.UpdateAPIView):
    queryset = models.Verification.objects.all()
    serializer_class = serializers.VerificationSerializer

class StripeReload(generics.ListCreateAPIView):
    queryset = models.Reload.objects.all()
    serializer_class = serializers.ReloadSerializer

class StripeReloadByUser(generics.ListCreateAPIView):
    serializer_class = serializers.ReloadSerializer

    def get_queryset(self):
        return models.Reload.objects.filter(user=self.kwargs['pk'])

class ViewBalance(generics.RetrieveAPIView):
    queryset = models.NyteUser.objects.all()
    serializer_class = serializers.ViewBalanceSerializer

class CategoryByVenue(generics.ListCreateAPIView):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        return models.Category.objects.filter(venue=self.kwargs['pk'])

class CategoryCreate(generics.CreateAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

class MenuItemByCategory(generics.ListAPIView):
    serializer_class = serializers.MenuItemSerializer
    pagination_class = None

    def get_queryset(self):
        return models.MenuItem.objects.filter(category=self.kwargs['pk'])

class OpenTransactions(generics.ListAPIView):
    serializer_class = serializers.TransactionSerializer

    def get_queryset(self):
        return models.Transaction.objects.all().exclude(status="picked up").exclude(status="canceled");

class MenuItemsByVenue(generics.ListAPIView):
    serializer_class = serializers.MenuItemSerializer

    def get_queryset(self):
        return models.MenuItem.objects.filter(venue=self.kwargs['pk']);

class OptionList(generics.ListAPIView):
    serializer_class = serializers.OptionSerializer
    queryset = models.MenuOption.objects.all()

class OptionListByVenue(generics.ListAPIView):
    serializer_class = serializers.OptionSerializer

    def get_queryset(self):
        queryset = set()
        venue = self.kwargs['pk']

        for item in models.OptionPairing.objects.all():
            if (item.menu_item.venue.id == venue):
                queryset.add(item.option.id)

        return models.MenuOption.objects.filter(pk__in=queryset)

class OpenTransactionsByVenue(generics.ListAPIView):
    serializer_class = serializers.TransactionSerializer

    def get_queryset(self):
        return models.Transaction.objects.filter(venue=self.kwargs['pk']).exclude(status="completed").exclude(status="canceled").exclude(status="picked up")