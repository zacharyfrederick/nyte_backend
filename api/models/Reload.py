from django.db import models

from .NyteUser import NyteUser
from ..managers import Stripe_Manager

class Reload(models.Model):
    stripe_id = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(NyteUser, on_delete=models.CASCADE)
    payment_source = models.CharField(max_length=100, blank=True)
    amount = models.FloatField(null=True)
    paid = models.BooleanField(default=False, blank=True)
    failure_code = models.CharField(max_length=50, blank=True, null=True)
    failure_message = models.CharField(max_length=100, blank=True, null=True)
    stripe_transaction_id = models.CharField(max_length=100, blank=True, null=True)
    
    STRIPE_ID_ERROR = "STRIPE_ID_ERROR"
    STRIPE_ID_ERROR_MESSAGE = "stripe_id does not exist for this user"

    PAYMENT_ERROR = "PAYMENT_ERROR"
    PAYMENT_ERROR_MESSAGE = "no payment is set for this user"

    def attempt_to_reload(self):
        self.stripe_manager = Stripe_Manager()
        self.set_stripe_id()
        if self.failure_code is not self.STRIPE_ID_ERROR:
            self.create_charge_and_get_results()

    def set_stripe_id(self):
        self.stripe_id = self.user.stripe_id

        if self.stripe_id == self.user.STRIPE_ID_DOES_NOT_EXIST:
            self.failure_code = self.STRIPE_ID_ERROR
            self.failure_message = self.STRIPE_ID_ERROR_MESSAGE

    def set_failure_state(self):
        self.failure_code = self.stripe_manager.get_failure_code()
        self.failure_message = self.stripe_manager.get_failure_message()
        
    def set_paid(self):
        self.paid = self.stripe_manager.get_paid()

    def set_stripe_transaction_id(self):
        self.stripe_transaction_id = self.stripe_manager.get_transaction_id()
    
    def set_payment_source(self):
        self.payment_source = self.stripe_manager.get_payment()

    def create_charge_and_get_results(self):
        self.stripe_manager.create_charge(self.user, int(self.amount*100))
        self.set_failure_state()
        self.set_paid()
        self.set_stripe_transaction_id()
        self.set_payment_source()