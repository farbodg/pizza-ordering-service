from rest_framework.response import Response
from rest_framework.views import status
from rest_framework import generics

from ..models import Customer
from ..serializers.customer import CustomerCreateSerializer


class CustomerCreateView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerCreateSerializer

    def post(self, request, *args, **kwargs):
        customer = Customer.objects.create(
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            address=request.data["address"],
            phone_number=request.data["phone_number"]
        )
        return Response(
            data=CustomerCreateSerializer(customer).data,
            status=status.HTTP_201_CREATED
        )

