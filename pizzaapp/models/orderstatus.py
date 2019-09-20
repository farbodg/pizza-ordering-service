from django.db import models


class OrderStatus(models.Model):
    label = models.CharField(max_length=255, null=False)