from django.db import models
from fcm_django.models import FCMDevice

class BartenderDevice(models.Model):
    device = models.ForeignKey(FCMDevice, on_delete=models.CASCADE)
    venue = models.ForeignKey('api.Venue', on_delete=models.CASCADE)