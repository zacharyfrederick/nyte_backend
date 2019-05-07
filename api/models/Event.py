from django.db import models
from .Venue import Venue

class Event(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    description = models.TextField(null=False, blank=False)
    start = models.DateTimeField(null=False, blank=False)
    end = models.DateTimeField(null=False, blank=False)
    is_active = models.BooleanField(default=False, null=False, blank=False)
    
