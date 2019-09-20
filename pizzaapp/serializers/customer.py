from rest_framework import serializers

from ..models import Customer


# Create customer serializer
class CustomerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ("id", )