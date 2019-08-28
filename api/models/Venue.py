from django.db import models
from .BartenderDevice import BartenderDevice
from fcm_django.models import FCMDevice

class Venue(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    music_type = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="venues/", null=True, default=None) #TODO: install pillow and change to image field
    markup_fee = models.FloatField(null=True, blank=True)
    sales_tax = models.FloatField(null=True, blank=True, default=6.0); #represents a 6% sales sax
    convenience_fee = models.FloatField(null=True, blank=True, default=0.5);
    minimum_age = models.IntegerField(default=21, blank=True)
    
    def __str__(self):
        return self.name;

    def update_bartender_devices(self):
        devices = BartenderDevice.objects.filter(venue=self.id)
        
        for device in devices:
            print("firing message to bartender device")
            fcm_device = device.device
            fcm_device.send_message(title="New Order", body="A new order was submitted", api_key="AAAAv4Tr6Zc:APA91bG20VhoPZhDvMhYWbjNE3RwO7Coxx-EhPTez2lEsz3JOAsa14q5X9Hxpr57ZLtXcfj7-gfWV1AXy5HfdcdmM6emK5tA-GyfrPoysFCHMpK_dmcbhz_iAGyAxDSh7NarrtDGY2W2")
            