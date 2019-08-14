from django.db import models
from .NyteUser import NyteUser
from ..managers import AgeCheckerManager
from drf_extra_fields.fields import Base64ImageField
from django.conf import settings
import stripe
from fcm_django.models import FCMDevice
from .PatronDevice import PatronDevice

VerificationChoices = (
    ("no", "Not Verified"),
    ("ac", "Accepted"),
)

class Verification(models.Model):
    user = models.OneToOneField(NyteUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    dob_day = models.CharField(max_length=100, default="")
    dob_month = models.CharField(max_length=100, default="")
    dob_year = models.CharField(max_length=100, default="")
    addr = models.CharField(max_length=150, default="")
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=50, default="")
    zipcode = models.CharField(max_length=10, default="")
    uuid = models.CharField(max_length=200, default="")
    verif_status = models.CharField(max_length=100, default="")
    attempted_to_verify = models.BooleanField(default=False)
    error_code = models.CharField(max_length=100, default="")
    error_msg = models.CharField(max_length=100, default="")
    image = models.ImageField(blank=False, null=True)
    stripe_id = models.CharField(max_length=100, null=True)
    fcm_token = models.CharField(max_length=250, default="", blank=True)

    unformatted_descr = "Stripe Account for Nyte user {} {}"

    def attempt_to_verify(self):
        attempted_to_verify = True
        manager = AgeCheckerManager()
        response = manager.attempt_to_verify(self)

        if self.fcm_token != "":
            fcm_device = FCMDevice.objects.create(registration_id=self.fcm_token)
            patron_device = PatronDevice.objects.create(fcm_device=fcm_device, user=self.user)

        if response is not None:
            if response.error_code is None:
                self.uuid = response.uuid
                self.verif_status = response.status

                if self.verif_status == "accepted":
                    self.create_stripe_account()
                    self.user.update_verification_info(self)
            else:
                self.error_code = response.error_code
                self.error_msg = response.error_msg

    def create_stripe_account(self):
        formatted_descr = self.unformatted_descr.format(self.first_name, self.last_name)
        try:
            customer = stripe.Customer.create(description=formatted_descr, email=self.email,
                name="{} {}".format(self.first_name, self.last_name))

            self.stripe_id = customer['id']
        except stripe.error.StripeError as e:
            print(e)
            return


