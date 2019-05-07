from django.db import models
from .Venue import Venue

class MenuItem(models.Model):
    ITEM_TYPE = (
        ("FO", "Food"),
        ("BE", "Beer"),
        ("WI", "Wine"),
        ("MI", "Mixed Drink"),
        ("SH", "Shot"),
    )

    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=300, null=True, blank=True)
    rating = models.FloatField(default=0.0, null=True, blank=True)
    item_type = models.CharField(max_length=100, null=False, blank=False, choices=ITEM_TYPE)
    
