from django.db import models
from .BartenderDevice import BartenderDevice
from fcm_django.models import FCMDevice

class Venue(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    music_type = models.CharField(max_length=100, blank=True, null=True)
    price_level = models.CharField(max_length=50, blank=True, null=True)
    crowd_size = models.CharField(max_length=50, blank=True, null=True)
    tagline = models.CharField(max_length=100, blank=False, null=True)
    image = models.CharField(max_length=100) #TODO: install pillow and change to image field
    markup_fee = models.FloatField(null=True, blank=True)
    sales_tax = models.FloatField(null=True, blank=True, default=6.0); #represents a 6% sales sax
    convenience_fee = models.FloatField(null=True, blank=True, default=0.5);
    
    def __str__(self):
        return self.name;

    def update_bartender_devices(self):
        devices = BartenderDevice.objects.filter(venue=self.id)
        
        for device in devices:
            print("firing message to bartender device")
            fcm_device = device.device
            fcm_device.send_message(title="New Order", body="A new order was submitted")
            