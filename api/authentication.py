from rest_framework import authentication
import json
from .managers import FacebookManager
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions

class NyteAuthentication(authentication.TokenAuthentication):
    def authenticate(self, request):
        try:
            fb_manager = FacebookManager()
            access_token = json.loads(request.body)['access_token']
        except KeyError:
            msg = _('Invalid facebook token. No Credentials provided')
            raise exceptions.AuthenticationFailed(msg)
        
        token_val_resp = fb_manager.send_request(access_token=access_token)
        
        if token_val_resp is None:
            msg = _('Facebook access_token invalid. User is logged out')
            raise exceptions.AuthenticationFailed(msg)

        auth = authentication.get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None
        
        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)