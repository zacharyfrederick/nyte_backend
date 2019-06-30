from django.db import models
from .NyteUser import NyteUser
from .Venue import Venue
from django.contrib.postgres.fields import JSONField
from ..managers import Stripe_Manager
import datetime 
import django

class Transaction(models.Model):
    user = models.ForeignKey(NyteUser, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, null=False, blank=True, default="submitted")
    placed = models.DateTimeField(null=True, blank=True, default=django.utils.timezone.now)
    ready = models.DateTimeField(null=True, blank=True)
    complete = models.DateTimeField(null=True, blank=True)
    canceled = models.DateTimeField(null=True, blank=True)
    cancal_reason = models.CharField(max_length=100, null=True, blank=True)
    total = models.FloatField(default=0.0, null=True)
    data = JSONField(null=True, blank=True)
    card = models.CharField(max_length=100, null=True, blank=True)
    failure_code = models.CharField(max_length=50, blank=True, null=True, default="None")
    failure_message = models.CharField(max_length=100, blank=True, null=True, default="None")
    stripe_transaction_id = models.CharField(max_length=100, blank=True, null=True)
    has_attempted_to_charge = models.BooleanField(blank=True, default=False)


    STRIPE_ID_ERROR = "STRIPE_ID_ERROR"
    STRIPE_ID_ERROR_MESSAGE = "stripe_id does not exist for this user"

    INSUFFICIENT_BALANCE_ERROR = "INSUFFICIENT_BALANCE"
    INSUFFICIENT_BALANCE_ERROR_MESSAGE = "Your account has an insufficient balance to make this transaction"

    def attempt_to_charge(self):
        self.has_attempted_to_charge = True
        self.stripe_manager = Stripe_Manager()
        self.check_stripe_id_is_valid()
        self.check_if_balance_is_enough()

        if self.failure_code is not self.STRIPE_ID_ERROR and self.failure_code is not self.INSUFFICIENT_BALANCE_ERROR:
            self.create_charge_and_get_results()

    def check_stripe_id_is_valid(self):
        if self.user.stripe_id is self.user.STRIPE_ID_DOES_NOT_EXIST:
            self.failure_code = self.STRIPE_ID_ERROR
            self.failure_message = self.STRIPE_ID_ERROR_MESSAGE

    def create_charge_and_get_results(self):
        self.stripe_manager.create_charge(customer=self.user, amount=int(self.total), card=self.card)
        self.set_failure_state()
        self.set_stripe_transaction_id()
        self.attempt_to_update_balance()

    def set_failure_state(self):
        self.failure_code = self.stripe_manager.get_failure_code()
        self.failure_message = self.stripe_manager.get_failure_message()

    def set_stripe_transaction_id(self):
        self.stripe_transaction_id = self.stripe_manager.get_transaction_id()

    def attempt_to_update_balance(self):
        if self.failure_code is "None":
            self.user.account_balance = self.user.account_balance - self.total
            self.user.save()

    def check_if_balance_is_enough(self):
        if self.user.account_balance < self.total:
            self.failure_code = self.INSUFFICIENT_BALANCE_ERROR
            self.failure_message = self.INSUFFICIENT_BALANCE_ERROR_MESSAGE
    