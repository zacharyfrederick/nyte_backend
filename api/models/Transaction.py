from django.db import models
from .NyteUser import NyteUser
from .Venue import Venue
from django.contrib.postgres.fields import JSONField

class Transaction(models.Model):
    user = models.ForeignKey(NyteUser, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, null=False, blank=True)
    eta = models.FloatField(default=0.0)
    data = JSONField()
    