"""Model for Orders"""
from django.db import models
from .Vendor import Vendor
from .Payment import Payment
from .Customer import Customer

class Order(models.Model):
    """
    vendor! - An order depends on a vendor
    customer! - Must have a customer for a valid order
    payment - On creation, payment will not be provided by the vendor
    start! - Must have a date and time for the event
    end! - Must have a date and time for the event
    location! - Must have a location for the event
    """
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    payment = models.ForeignKey(Payment, on_delete=models.DO_NOTHING, blank=True, null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    location = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("order")
        verbose_name_plural = ("orders")