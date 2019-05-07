from django.db import models
from .Venue import Venue

class WorksAt(models.Model):
    ROLE_TYPE = (
        ("OW", "Owner"),
        ("BA", "Bartender"),
    )

    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, null=False, blank=False, choices=ROLE_TYPE)
