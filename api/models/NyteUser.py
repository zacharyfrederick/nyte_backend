from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.db import models
from .WorksAt import WorksAt
from ..managers import CustomUserManager

class NyteUser(AbstractUser):
    USER_TYPE = (
        ("PA", "Patron"),
        ("OW", "Owner"),
        ("BA", "Bartender"),
    )

    birthday = models.DateField(blank=False, null=True)
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

    objects = CustomUserManager()
