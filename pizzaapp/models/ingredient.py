from django.db import models


class Ingredient(models.Model):
    display_name = models.CharField(max_length=255, null=False)
    code = models.CharField(max_length=10, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=4, null=False)