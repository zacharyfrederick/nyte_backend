from django.db import models
from .Venue import Venue
from .AccountInformation import AccountInformation

class Account(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    amount = models.FloatField()
    payout_date = models.DateTimeField()
    bank_account = models.ForeignKey(AccountInformation, on_delete=models.CASCADE)
