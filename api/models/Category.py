from django.db import models

from .Venue import Venue as NyteVenue

class Category(models.Model):
    venue = models.ForeignKey(NyteVenue, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name