from django.db import models
from .NyteUser import NyteUser

class Identity(models.Model):
    user = models.ForeignKey(NyteUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    id_img = models.CharField(max_length=100) #TODO: update to imagefield and install pillow
