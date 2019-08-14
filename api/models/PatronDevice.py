from django.db import models
from fcm_django.models import FCMDevice
from .NyteUser import NyteUser

class PatronDevice(models.Model):
    fcm_device = models.ForeignKey(FCMDevice, on_delete=models.CASCADE)
    user = models.ForeignKey(NyteUser, on_delete=models.CASCADE)