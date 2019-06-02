from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    music_type = models.CharField(max_length=100, blank=True, null=True)
    price_level = models.CharField(max_length=50, blank=True, null=True)
    crowd_size = models.CharField(max_length=50, blank=True, null=True)
    tagline = models.CharField(max_length=100, blank=False, null=True)
    image = models.CharField(max_length=100) #TODO: install pillow and change to image field
    markup_fee = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.name;