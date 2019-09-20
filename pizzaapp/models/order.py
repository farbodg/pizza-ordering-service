from django.db import models
from .orderstatus import OrderStatus
from .customer import Customer


class Order(models.Model):
    total_price = models.DecimalField(decimal_places=2, max_digits=4, null=False)
    status = models.ForeignKey(OrderStatus, related_name='order', on_delete=models.CASCADE, null=False)
    customer = models.ForeignKey(Customer, related_name='order', on_delete=models.CASCADE, null=False)
    placed_datetime = models.DateTimeField(null=False)
    delivery_datetime = models.DateTimeField(null=True)

