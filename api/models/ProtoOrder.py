from django.db import models
from enum import Enum
from .. managers import TwilioManager

order_status_choices = (
    ("or", "Ordered"),
    ("ma", "Making"),
    ("re", "Ready"),
    ("pi", "Picked up"),
)

class ProtoOrder(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    phone_num = models.CharField(max_length=20, null=False, blank=False)
    status = models.CharField(max_length=100, null=False, blank=False, default="or", choices=order_status_choices)
    message_sent = models.BooleanField(default=False, blank=True)

    def should_msg_be_sent(self):
        return True if self.status == "re" and self.message_sent == False else False

    def send_msg(self):
        self.message_sent = True
        twilio_manager = TwilioManager()
        twilio_manager.send_sms_message(self.phone_num, "Your order is ready for pickup! Enjoy your nyte.")



    