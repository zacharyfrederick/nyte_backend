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
from django.http import JsonResponse
import base64
from django.core.files import File

class NyteUser(AbstractUser):
    USER_TYPE = (
        ("PA", "Patron"),
        ("OW", "Owner"),
        ("BA", "Bartender"),
    )
    NO_DEFAULT_PAYMENT = "None"
    STRIPE_ID_DOES_NOT_EXIST = "None"

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    dob_day = models.CharField(max_length=100, default="")
    dob_month = models.CharField(max_length=100, default="")
    dob_year = models.CharField(max_length=100, default="")
    user_type = models.CharField(max_length=100, blank=False, null=True, choices=USER_TYPE, default="PA")
    is_age_verified = models.BooleanField(default=False, blank=False, null=False)
    is_email_verified = models.BooleanField(default=False, blank=False, null=False)
    membership = models.ManyToManyField(WorksAt, blank=True)
    public_key = models.CharField(max_length=500, blank=True, null=True)
    private_key = models.CharField(max_length=2000, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    first_name = models.CharField(('first name'), max_length=30, null=True)
    last_name = models.CharField(('last name'), max_length=50, null=True)
    middle_name = models.CharField(
        max_length=64, verbose_name=('middle name'), blank=True, null=True)
    phone = models.CharField(max_length=64, verbose_name=('user phone'), null=True)
    facebook_id = models.CharField(max_length=200, unique=True, null=True)
    profile_image = models.CharField(max_length=300, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    is_verified = models.BooleanField(default=False, blank=True)
    id_image = models.ImageField(upload_to="users/", null=True, default="None");
    stripe_id = models.CharField(max_length=100, null=True, default=STRIPE_ID_DOES_NOT_EXIST)
    account_balance = models.IntegerField(null=True, default=0)
    default_payment = models.CharField(max_length=100, null=True, default=NO_DEFAULT_PAYMENT)


    objects = NyteUserManager()

    class meta:
        unique_together = ('addr', 'first_name', 'last_name', 'dob_day', 'dob_month', 'dob_year' )
        
    def login_json_response(self, access_token):
        token = Token.objects.get(user=self.id)
        return JsonResponse({
            "user_id": self.id,
            "nyte_token": token.key,
            "access_token": access_token,
            "is_verified": self.is_verified,
        })

    def update_verification_info(self, verification):
        self.first_name = verification.first_name
        self.last_name = verification.last_name
        self.dob_day = verification.dob_day
        self.dob_month = verification.dob_month
        self.dob_year = verification.dob_year
        self.email = verification.email
        self.stripe_id = verification.stripe_id
        self.is_verified = True
        self.save()
    