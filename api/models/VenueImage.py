from django.db import models
from .Venue import Venue

class VenueImage(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="venue_images/")
    name = models.CharField(max_length=200)
    descr = models.CharField(max_length=200)
    