class TokenRequestResponse():
    def __init__(self, user_id, access_token, refresh_interval):
        self.id = user_id
        self.access_token = access_token
        self.refresh_interval = refresh_interval

class TokenValidationResponse:
    def __init__(self,id, phone,app_id):
        self.id = id
        self.phone = phone
        self.app_id = app_id

class AgeCheckerResponse:
    def __init__(self, uuid=None, status=None, error_msg=None, error_code=None):
        self.uuid = uuid
        self.status = status
        self.error_msg = error_msg
        self.error_code = error_code