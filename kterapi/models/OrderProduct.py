from django.db import models
from .Order import Order
from .Product import Product

class OrderProduct(models.Model):

    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("orderproduct")
        verbose_name_plural = ("orderproducts")