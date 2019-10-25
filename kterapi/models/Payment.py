from django.db import models
from .Customer import Customer

class Payment(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    merchant_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    expiration = models.DateField(max_length=255)

    class Meta:
        verbose_name = ("payment")
        verbose_name_plural = ("payments")