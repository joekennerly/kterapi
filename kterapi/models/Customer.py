from django.db import models

class Customer(models.Model):

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("customer")
        verbose_name_plural = ("customers")