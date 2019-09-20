from django.db import models
from .pizza import Pizza
from .ingredient import Ingredient


class PizzaIngredient(models.Model):
    pizza = models.ForeignKey(Pizza, related_name='pizzaingredient', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, related_name='pizzaingredient', on_delete=models.CASCADE)