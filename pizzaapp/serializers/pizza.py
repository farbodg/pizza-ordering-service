from rest_framework import serializers

from ..models import Pizza, PizzaIngredient, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        exclude = ("id", "price")


class PizzaIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(read_only=True)

    class Meta:
        model = PizzaIngredient
        depth = 1
        exclude = ("id", "pizza")


class PizzaSerializer(serializers.ModelSerializer):
    pizzaingredient = PizzaIngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Pizza
        depth = 1
        exclude = ("id", "order")