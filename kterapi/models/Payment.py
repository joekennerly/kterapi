from django.db import models
from .Customer import Customer

class Payment(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    merchant_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    expiration = models.DateField()

    class Meta:
        verbose_name = ("payment")
        verbose_name_plural = ("payments")