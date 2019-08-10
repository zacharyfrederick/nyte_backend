from django.db import models
from .MenuItem import MenuItem
from .Category import Category
from .Option import MenuOption

class OptionPairing(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="pairings")
    option = models.ForeignKey(MenuOption, on_delete=models.CASCADE)
