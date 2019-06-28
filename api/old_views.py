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
from rest_framework.parsers import FileUploadParser
from rest_framework import status
import stripe

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

# @csrf_exempt
# def login_view(request):
#     if request.method == "POST":
#         try:
#             new_user = False
#             auth_code = json.loads(request.body)['authorization_code']
#             fb_manager = FacebookManager()
#             access_token_resp = fb_manager.send_request(auth_code=auth_code)
#             if access_token_resp is not None:
#                 if models.NyteUser.objects.filter(facebook_id=access_token_resp.id).exists():
#                     nyte_user = models.NyteUser.objects.get(facebook_id=access_token_resp.id)
#                 else:
#                     access_token_val_resp = fb_manager.send_request(access_token=access_token_resp.access_token)
#                     if access_token_val_resp is not None:
#                         nyte_user = models.NyteUser.objects.create(facebook_id=access_token_resp.id, phone=access_token_val_resp.phone)
#                     else:
#                         nyte_user = models.NyteUser.objects.create(facebook_id=access_token_resp.id)
#                 return nyte_user.login_json_response(access_token_resp.access_token)
#             else:
#                 return JsonResponse({"error": "invalid credentials supplied"}, safe=False)
#         except KeyError:
#             return JsonResponse({"error": "authorization_code not supplied"}, safe=False)
#     else:
#         return JsonResponse({"error": "only POST allowed to this url"}, safe=False)

@csrf_exempt
def fb_logout_view(request):
    if request.method == "POST":
        try:
            access_token = json.loads(request.body)['access_token']
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

class VerificationIdUpload(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request,  *args, **kwargs):
        file_serializer = serializers.VerificationIDSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        images = models.VerificationID.objects.all()
        serializer = serializers.VerificationIDSerializer(images, many=True)
        return Response(serializer.data)

class EphemeralKeyView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            user_id = json.loads(request.body)['user']
            api_version = json.loads(request.body)['api_version']
            try:
                user = models.NyteUser.objects.get(id=user_id)
                key = stripe.EphemeralKey.create(customer=user.stripe_id, stripe_version=api_version)
                return Response({"key": key})
            except models.NyteUser.DoesNotExist:
                return Response({"error": "Invalid user_id"})
        except KeyError as e:
            print(e)
            return Response({"error": "invalid credentials supplied"})