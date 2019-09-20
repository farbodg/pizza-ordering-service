from django.db import models
from .order import Order


class Pizza(models.Model):
    order = models.ForeignKey(Order, related_name='pizzas', on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    size = models.CharField(max_length=2, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=4, null=False)

