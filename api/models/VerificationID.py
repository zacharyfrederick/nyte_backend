from django.db import models
from . import Verification

class VerificationID(models.Model):
    image = models.ImageField(upload_to="staticfiles/id_images/", blank=False, null=False)
    verification = models.OneToOneField(Verification, blank=False, null=True, unique=True, on_delete=models.CASCADE)
