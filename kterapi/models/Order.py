from django.db import models
from .Vendor import Vendor
from .Payment import Payment
from .Customer import Customer

class Order(models.Model):

    vendor = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    payment = models.ForeignKey(Payment, on_delete=models.DO_NOTHING, blank=True, null=True)
    event_date = models.DateTimeField()

    class Meta:
        verbose_name = ("order")
        verbose_name_plural = ("orders")