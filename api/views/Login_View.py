#python imports
import json

#django imports
from django.views.decorators.csrf import csrf_exempt

#DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response

#Nyte imports
from ..managers import FacebookManager
from .. import models

class LoginView(APIView):
    #errors
    AUTHORIZATION_CODE_NOT_SUPPLIED_ERROR = {"error": "authorization_code not supplied"}
    INVALID_FB_CREDENTIALS_ERROR = {"error": "invalid fb credentials supplied"}
    INVALID_HTTP_VERB_ERROR = {"error": "only POST allowed to this url"}

    def __init__(self):
        self.facebook = FacebookManager()

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        auth_code = self.get_auth_code_or_return_error(request)
        access_token_response = self.facebook.send_request(auth_code=auth_code)
        user = self.get_user_with_response_data(access_token_response)
        return user.login_json_response(access_token_response.access_token)

    def get_auth_code_or_return_error(self, request):
        try:
            auth_code = json.loads(request.body)['authorization_code']
            return auth_code
        except KeyError:
            return Response(self.AUTHORIZATION_CODE_NOT_SUPPLIED_ERROR)
        except json.JSONDecodeError:
            return Response("Something went wrong")

    def get_user_with_response_data(self, response):
        if response is not None:
            return self.get_or_create_user_with_fb_id(fb_id=response.id, access_token=response.access_token)
        else:
            return Response(self.INVALID_FB_CREDENTIALS_ERROR)

    def get_or_create_user_with_fb_id(self, fb_id, access_token):
        if models.NyteUser.objects.filter(facebook_id=fb_id).exists():
            return models.NyteUser.objects.get(facebook_id=fb_id)
        else:
            return self.create_user_with_fb_id(fb_id, access_token)

    def create_user_with_fb_id(self, fb_id, access_token):
        phone = self.get_user_phone_with_access_token(access_token=access_token)
        return models.NyteUser.objects.create(facebook_id=fb_id, phone=phone)
    
    def get_user_phone_with_access_token(self, access_token):
        access_token_validation_response = self.facebook.send_request(access_token=access_token)
        return access_token_validation_response.phone

    def invalid_http_verb_called(self):
        return Response(self.INVALID_HTTP_VERB_ERROR)

    def get(self, request, *args, **kwargs):
        return self.invalid_http_verb_called()
    
    def put(self, request, *args, **kwargs):
        return self.invalid_http_verb_called()
    
    def patch(self, request, *args, **kwargs):
        return self.invalid_http_verb_called()
    
    def delete(self, request, *args, **kwargs):
        return self.invalid_http_verb_called()