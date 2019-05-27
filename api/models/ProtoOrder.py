from django.db import models

order_status_choices = (
    ("or", "Ordered"),
    ("ma", "Making"),
    ("re", "Ready"),
    ("pi", "Picked up")
)

class ProtoOrder(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    phone_num = models.CharField(max_length=20, null=False, blank=False)
    status = models.CharField(max_length=100, null=False, blank=False, default="or", choices=order_status_choices)
    