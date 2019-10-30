from django.db import models
from .Vendor import Vendor

class Customer(models.Model):

    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("customer")
        verbose_name_plural = ("customers")