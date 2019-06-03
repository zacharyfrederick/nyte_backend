from . import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(pre_save, sender=models.ProtoOrder)
def proto_order_pre_save(sender, **kwargs):
    proto_order = kwargs.get("instance")
    if proto_order.should_msg_be_sent():
        proto_order.send_msg()
        
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)