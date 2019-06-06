from django.db import models
from .NyteUser import NyteUser
from ..managers import AgeCheckerManager

VerificationChoices = (
    ("no", "Not Verified"),
    ("ac", "Accepted"),
)

class Verification(models.Model):
    user = models.OneToOneField(NyteUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    dob_day = models.CharField(max_length=100, default="")
    dob_month = models.CharField(max_length=100, default="")
    dob_year = models.CharField(max_length=100, default="")
    addr = models.CharField(max_length=150, default="")
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=50, default="")
    zipcode = models.CharField(max_length=10, default="")
    uuid = models.CharField(max_length=200, default="")
    status = models.CharField(max_length=100, default="")
    attempted_to_verify = models.BooleanField(default=False)
    error_code = models.CharField(max_length=100, default="")
    error_msg = models.CharField(max_length=100, default="")

    def attempt_to_verify(self):
        attempted_to_verify = True
        manager = AgeCheckerManager()
        response = manager.attempt_to_verify(self)

        if response is not None:
            if response.error_code is None:
                self.uuid = response.uuid
                self.status = response.status

                if self.status == "accepted":
                    self.user.update_verification_info(self)
            else:
                self.error_code = response.error_code
                self.error_msg = response.error_msg
            


