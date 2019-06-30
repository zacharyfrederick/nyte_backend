from ..helpers import AgeCheckerResponse
import requests

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