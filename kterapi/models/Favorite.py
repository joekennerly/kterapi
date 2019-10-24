from django.db import models
from .Customer import Customer
from .Vendor import Vendor

class Favorite(models.Model):

    vendor = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("favorite")
        verbose_name_plural = ("favorites")