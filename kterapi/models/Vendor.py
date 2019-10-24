from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Vendor(models.Model):
    """Vendors are the main users of this application"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    bio = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = ("vendor")
        verbose_name_plural = ("vendors")