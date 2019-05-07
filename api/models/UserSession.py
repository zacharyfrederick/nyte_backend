from django.db import models
from .NyteUser import NyteUser

class UserSession(models.Model):
    user = models.ForeignKey(NyteUser, on_delete=models.CASCADE)
    encryption_key = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()
    is_active = models.BooleanField()