from rest_framework import serializers

from ..models import Order
from .pizza import PizzaSerializer
from .customer import CustomerCreateSerializer


# Get all orders serializer
class OrderListSerializer(serializers.ModelSerializer):
    customer = CustomerCreateSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ("id", "customer", "total_price")


# Order Details serializer
class OrderDetailsSerializer(serializers.ModelSerializer):
    pizzas = PizzaSerializer(many=True, read_only=True)
    customer = CustomerCreateSerializer(read_only=True)

    class Meta:
        model = Order
        depth = 1
        fields = ("id", "status", "total_price", "placed_datetime", "delivery_datetime", "customer", "pizzas")

    status = serializers.SerializerMethodField("get_status_label")

    def get_status_label(self, obj):
        return obj.status.label


# Place order serializer
class OrderPlacedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "status", "total_price", "customer", "placed_datetime")


# Get order status serializer
class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "status")

    status = serializers.SerializerMethodField("get_status_label")

    def get_status_label(self, obj):
        return obj.status.label