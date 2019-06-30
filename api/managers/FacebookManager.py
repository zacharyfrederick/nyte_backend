import requests

from django.conf import settings
from ..helpers import TokenRequestResponse, TokenValidationResponse 

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

    def get_access_token(self, auth_code):
        formatted_url = self.create_token_request_url(auth_code)
        response = requests.get(url=formatted_url)
        return self.interpret_json(response, self.read_token_request_json)
        

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