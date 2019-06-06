from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import requests
from collections import namedtuple
from twilio.rest import Client
from .helpers import TokenRequestResponse, TokenValidationResponse, AgeCheckerResponse

class AgeCheckerManager():
    VERIFICATION_URL = "https://api.agechecker.net/v1/create"
    DEFAULT_COUNTRY = "US"

    def build_request_data(self, verification):
        data = {
            "key": "xmTU0wA12zFhg2mZmiQ0ookNoSUZ68S4",
            "secret": "yqKqNATKU00yA1ie",
            "data": {
                "address": verification.addr,
                "city": verification.city,
                "country": self.DEFAULT_COUNTRY,
                "dob_day": verification.dob_day,
                "dob_month": verification.dob_month,
                "dob_year": verification.dob_year,
                "first_name": verification.first_name,
                "last_name": verification.last_name,
                "state": verification.state,
                "zip": verification.zipcode
            }
        }
        return data
        
    def interpret_json(self, response):
        try:
            json = response.json()
            if "error" not in json:
                return AgeCheckerResponse(uuid=json['uuid'], status=json['status'])
            else:
                return AgeCheckerResponse(error_msg=json['error']['message'], error_code=json['error']['code'])
        except ValueError:
            return None
            
    def attempt_to_verify(self, verification):
        return self.interpret_json(requests.post(url=self.VERIFICATION_URL, json=self.build_request_data(verification)))

class TwilioManager():
    def send_sms_message(self, to_num, msg):
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILI_AUTH_TOKEN)
        message = client.create(to_num, settings.TWILIO_FROM_NUM, msg);

class FacebookManager():
    RAW_TOKEN_REQUEST_URL = "https://graph.accountkit.com/v1.3/access_token?grant_type=authorization_code&code={}&access_token=AA|{}|{}"
    RAW_ACCESS_TOKEN_URL = "https://graph.accountkit.com/v1.3/me/?access_token={}"
    RAW_LOGOUT_URL = "https://graph.accountkit.com/v1.3/logout?access_token={}"

    def create_logout_url(self, access_token):
        return self.RAW_LOGOUT_URL.format(access_token)

    def create_token_request_url(self, auth_code):
        return self.RAW_TOKEN_REQUEST_URL.format(auth_code, settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET)
    
    def create_access_token_url(self, access_token):
        return self.RAW_ACCESS_TOKEN_URL.format(access_token)

    def read_token_request_json(self, json):
        return TokenRequestResponse(json['id'], json['access_token'], json['token_refresh_interval_sec'])

    def read_token_val_json(self, json):
        return TokenValidationResponse(json['id'], json['phone']['number'], json['application']['id'])

    def read_logout_json(self, json):
        return json 

    def interpret_json(self, request, json_method):
        try:
            json = request.json()
            if "error" not in json:
                response = json_method(json)
                return response
            else:
                print(json)
                return None
        except ValueError:
            return None

    def send_request(self, auth_code=None, access_token=None, logout=None):
        formatted_url = None
        json_method = None

        if auth_code is not None and access_token is not None and logout is not None:
            return None

        if auth_code is not None:
            formatted_url = self.create_token_request_url(auth_code)
            json_method = self.read_token_request_json

        if access_token is not None and logout is None:
            formatted_url = self.create_access_token_url(access_token)
            json_method = self.read_token_val_json
        
        if logout is True:
            formatted_url = self.create_logout_url(access_token)
            json_method = self.read_logout_json

        if logout is None:
            request = requests.get(url=formatted_url)
        elif logout is True:
            request = requests.post(url=formatted_url)
            
        response = self.interpret_json(request, json_method)
        return response

class NyteUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)