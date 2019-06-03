from . import serializers
from . import models
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from . import forms
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import facebook
import json
from .managers import FacebookManager
from rest_framework.permissions import IsAuthenticated
from .authentication import NyteAuthentication

#might need to delete this idk if we will use it
class CreateNyteUser(APIView):
    def post(self, request, format=None):
        form = forms.NyteUserCreationForm(request.POST)
        if (form.is_valid()):
            email=form.cleaned_data['email']
            password = form.cleaned_data['password1']
            new_user = models.NyteUser.objects.create(email=email, password=password)
            token = Token.objects.get(user=new_user.id)
            return Response({
                "token": token.key,
                "user_id": new_user.id
            })   
        else:
            if models.NyteUser.objects.filter(email=request.POST.get('email')).exists():
                return Response({"Error": "A user with that email already exists"})
            return Response({"Error": "Invalid form values provided"})

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
    authentication_classes = (NyteAuthentication,)
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

@csrf_exempt
def login_view(request):
    print(request.body)
    if request.method == "POST":
        try:
            new_user = False
            auth_code = request.POST['authorization_code']
            fb_manager = FacebookManager()
            access_token_resp = fb_manager.send_request(auth_code=auth_code)
            if access_token_resp is not None:
                if models.NyteUser.objects.filter(facebook_id=access_token_resp.id).exists():
                    nyte_user = models.NyteUser.objects.get(facebook_id=access_token_resp.id)
                else:
                    new_user = True
                    nyte_user = models.NyteUser.objects.create(facebook_id=access_token_resp.id)
                return nyte_user.login_json_response(access_token_resp.access_token, new_user)
            else:
                return JsonResponse({"error": "invalid credentials supplied"}, safe=False)
        except KeyError:
            return JsonResponse({"error": "authorization_code not supplied"}, safe=False)
    else:
        return JsonResponse({"error": "only POST allowed to this url"}, safe=False)

@csrf_exempt
def fb_logout_view(request):
    if request.method == "POST":
        try:
            access_token = request.POST['access_token']
            fb_manager = FacebookManager()
            request_resp = fb_manager.send_request(access_token=access_token, logout=True)
            if request_resp is not None:
                return JsonResponse(request_resp, safe=False)
            else:
                return JsonResponse({"error": "an error occurred"})
        except KeyError:
            return JsonResponse({"error": "no access_token supplied"})
    else:
        return JsonResponse({"error": "only POST allowed to this url"})