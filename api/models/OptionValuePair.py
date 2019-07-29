from django.db import models
from .Option import MenuOption
from .OptionValue import OptionValue
from .Transaction import Transaction

class OptionValuePair(models.Model):
    option = models.ForeignKey(MenuOption, on_delete=models.CASCADE)
    value = models.ForeignKey(OptionValue, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)      