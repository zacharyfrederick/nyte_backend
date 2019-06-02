from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext as _
from django.db import models
from .WorksAt import WorksAt
from ..managers import NyteUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.utils import timezone

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
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    first_name = models.CharField(('first name'), max_length=30, null=True)
    last_name = models.CharField(('last name'), max_length=50, null=True)
    middle_name = models.CharField(
        max_length=64, verbose_name=('middle name'), blank=True)
    phone = models.CharField(max_length=64, verbose_name=('user phone'), null=True)
    facebook_id = models.CharField(max_length=200, unique=True, null=True)
    profile_image = models.CharField(max_length=300, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = NyteUserManager()
