from django.db import models
from .NyteUser import NyteUser
from .Venue import Venue
from django.contrib.postgres.fields import JSONField
from ..managers import Stripe_Manager
import datetime 
import django
import json
from .MenuItem import MenuItem

class MenuItemHelper():
    def __init__(self, item_id, quantity):
        self.item_id = item_id
        self.quantity = quantity
        self.get_data_with_id()

    def get_data_with_id(self):
        menu_item = MenuItem.objects.get(id=self.item_id)
        self.price = menu_item.price
        self.convenience_fee = menu_item.convenience_fee
        self.name = menu_item.name

    def to_json(self):
        return { "id": self.item_id, "quantity": self.quantity, "name" : self.name, "price": self.price, "convenience_fee" : self.convenience_fee}



class Transaction(models.Model):
    user = models.ForeignKey(NyteUser, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, null=False, blank=True, default="submitted")
    placed = models.DateTimeField(null=True, blank=True, default=django.utils.timezone.now)
    ready = models.DateTimeField(null=True, blank=True)
    complete = models.DateTimeField(null=True, blank=True)
    canceled = models.DateTimeField(null=True, blank=True)
    cancel_reason = models.CharField(max_length=100, null=True, blank=True)
    total = models.IntegerField(default=0, null=True)
    data = JSONField(null=True, blank=True)
    failure_code = models.CharField(max_length=50, blank=True, null=True, default="None")
    failure_message = models.CharField(max_length=100, blank=True, null=True, default="None")
    stripe_transaction_id = models.CharField(max_length=100, blank=True, null=True)
    has_attempted_to_charge = models.BooleanField(blank=True, default=False)
    is_completed = models.BooleanField(default=False, blank=True)
    is_data_formatted = models.BooleanField(default=False, blank=True)


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
        self.stripe_manager.create_charge(customer=self.user, amount=self.total, card=self.card)
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
    
    def format_data(self):
        menu_items = {}

        for index, menu_item_id in enumerate(self.data):
            menu_item = MenuItemHelper(item_id=menu_item_id, quantity=self.data[menu_item_id])
            menu_items[index] = menu_item.to_json()

        self.data = menu_items
        self.is_data_formatted = True
        
