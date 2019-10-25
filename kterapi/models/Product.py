from django.db import models
from .Vendor import Vendor
from .ProductCategory import ProductCategory

class Product(models.Model):

    name = models.CharField(max_length=50)
    vendor = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING, related_name='products')
    productcategory = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = ("product")
        verbose_name_plural = ("products")