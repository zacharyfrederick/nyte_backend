from django.db import models
from .Venue import Venue
from .Category import Category

class MenuItem(models.Model):
    ITEM_TYPE = (
        ("FO", "Food"),
        ("BE", "Beer"),
        ("WI", "Wine"),
        ("MI", "Mixed Drink"),
        ("SH", "Shot"),
    )

    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=300, null=True, blank=True)
    rating = models.FloatField(default=0.0, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0, null=True, blank=True)
    convenience_fee = models.FloatField(null=True, blank=True, default=-1.0);
    image = models.ImageField(upload_to="menu_items/",blank=True, null=True)

    def __str__(self):
        return self.name