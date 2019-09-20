from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=255, null=False)

