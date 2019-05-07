from django.db import models
from django.contrib.postgres.fields import JSONField
from .Venue import Venue

class Special(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    tagline = models.CharField(max_length=200, blank=False, null=False)
    start = models.DateTimeField(blank=False, null=False)
    end = models.DateTimeField(blank=False, null=False)
    is_active = models.BooleanField(default=False, blank=False, null=False)
    data = JSONField()
    