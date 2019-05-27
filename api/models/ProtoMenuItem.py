from django.db import models

item_choices = (
    ("sp", "Special"),
    ("be", "Beer"),
    ("wi", "Wine"),
    ("co", "Cocktail"),
    ("so", "Soda"),
    ("li", "Liquor")
)

class ProtoMenuItem(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    item_type = models.CharField(max_length=100, null=False, blank=False, choices=item_choices, default="be")
    image_url = models.URLField(max_length=200)