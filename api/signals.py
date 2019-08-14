from . import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
import json

@receiver(pre_save, sender=models.ProtoOrder)
def proto_order_pre_save(sender, **kwargs):
    proto_order = kwargs.get("instance")
    if proto_order.should_msg_be_sent():
        #proto_order.send_msg()
        pass
        
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
@receiver(pre_save, sender=models.Verification)
def attempt_to_verifiy(sender, **kwargs):
        verification_obj = kwargs.get("instance")
        if verification_obj.attempted_to_verify == False:
                verification_obj.attempt_to_verify()

@receiver(pre_save, sender=models.Reload)
def attempt_to_reload_balance(sender, **kwargs):
        reload_obj = kwargs.get("instance")
        if reload_obj.has_attempted_to_reload == False:
                reload_obj.attempt_to_reload()

@receiver(post_save, sender=models.Transaction)
def attempt_to_charge_transaction(sender, **kwargs):
        transaction = kwargs.get("instance")
        if transaction.is_data_formatted is False:
                #transaction.format_data()
                pass
        if transaction.has_attempted_to_charge is not True:
                transaction.attempt_to_charge()

@receiver(pre_save, sender=models.Transaction)
def check_for_status_updates(sender, **kwargs):
        transaction_id = kwargs.get("instance").id
        transaction = models.Transaction.objects.get(id=transaction_id)
        transaction.check_for_status_updates()
        print("Checking for status updates")
        
@receiver(pre_save, sender=models.MenuItem)
def set_default_convenience_fee(sender, **kwargs):
        menu_item = kwargs.get("instance")
        if menu_item.convenience_fee == -1.0:
                menu_item.convenience_fee = menu_item.venue.convenience_fee
                

        