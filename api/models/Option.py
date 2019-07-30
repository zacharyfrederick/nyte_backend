from django.db import models
from .MenuItem import MenuItem
from .Category import Category

class MenuOption(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    multiple_allowed = models.BooleanField(default=False, blank=True, null=True)
    required = models.BooleanField(default=False, blank=True, null=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, default=1, related_name='options')

    def __str__(self):
        return self.name
