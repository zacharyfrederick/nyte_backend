from django.db import models
from .NyteUser import NyteUser

VerificationChoices = (
    ("no", "Not Verified"),
    ("ac", "Accepted"),
)

class Verification(models.Model):
    user = models.OneToOneField(NyteUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    addr = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    uuid = models.CharField(max_length=200)
    status = models.CharField(max_length=100, default="no", choices=VerificationChoices)