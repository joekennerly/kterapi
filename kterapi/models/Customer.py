from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("customer")
        verbose_name_plural = ("customers")