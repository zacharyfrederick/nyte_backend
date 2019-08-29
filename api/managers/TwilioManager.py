from django.conf import settings
from twilio.rest import Client

class TwilioManager():
    def __init__(self):
        self.client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    def send_msg(self, to, msg):
        self.client.messages.create(to="to",from_="+13212042654", body="Your order is ready")