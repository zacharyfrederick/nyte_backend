from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.db import models
from .WorksAt import WorksAt
from ..managers import NyteUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    
class NyteUser(AbstractUser):
    USER_TYPE = (
        ("PA", "Patron"),
        ("OW", "Owner"),
        ("BA", "Bartender"),
    )

    birthday = models.DateField(blank=True, null=True)
    user_type = models.CharField(max_length=100, blank=False, null=False, choices=USER_TYPE)
    is_age_verified = models.BooleanField(default=False, blank=False, null=False)
    is_email_verified = models.BooleanField(default=False, blank=False, null=False)
    membership = models.ManyToManyField(WorksAt)
    public_key = models.CharField(max_length=500, blank=True, null=True)
    private_key = models.CharField(max_length=2000, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = NyteUserManager()
