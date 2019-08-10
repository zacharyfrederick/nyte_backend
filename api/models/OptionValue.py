from django.db import models
from .Option import MenuOption

class OptionValue(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(default=0, null=True, blank=True)
    default = models.BooleanField(default=False, blank=True, null=True)
    #option = models.ForeignKey(MenuOption, on_delete=models.CASCADE, default=None, related_name='values')    
