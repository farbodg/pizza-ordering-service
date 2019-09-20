from rest_framework.response import Response
from rest_framework.views import status
from rest_framework import generics

from django.http import HttpResponse

from ..models import Order
from ..serializers import OrderPlacedSerializer, OrderListSerializer, OrderStatusSerializer, OrderDetailsSerializer
from ..services import OrderService


# Return all orders, or creates a new order
class OrderListCreateView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    order_service = OrderService()

    # GET order/
    queryset = Order.objects.all()

    # POST order/
    def post(self, request, *args, **kwargs):
        try:

            order = self.order_service.place_order(request.data)

            return Response(
                data=OrderPlacedSerializer(order).data,
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            print(e)
            return Response(
                data={
                    "message": "error"
                },
                status=status.HTTP_404_NOT_FOUND
            )


# Retrieve/modify/delete order specified by id
class OrderDetailModifyDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailsSerializer
    order_service = OrderService()

    # GET order/:id
    def get(self, request, *args, **kwargs):
        order = Order.objects.get(pk=kwargs["id"])

        return Response(
            data=OrderDetailsSerializer(order).data,
            status=status.HTTP_200_OK
        )

    # POST order/:id
    def post(self, request, *args, **kwargs):
        order_id = kwargs["id"]

        order = self.order_service.update_order(order_id, request.data)

        return Response(
            data=OrderDetailsSerializer(order).data,
            status=status.HTTP_200_OK
        )

    # DELETE order/:id
    def delete(self, request, *args, **kwargs):
        order_id = kwargs["id"]

        delete_response = self.order_service.delete_order(order_id)

        return Response(
            data=delete_response,
            status=status.HTTP_200_OK
        )


class OrderStatusView(generics.ListAPIView):
    serializer_class = OrderStatusSerializer
    order_service = OrderService()

    def get(self, request, *args, **kwargs):
        order = Order.objects.get(pk=kwargs["id"])

        return Response(
            data=OrderStatusSerializer(order).data,
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        self.order_service.update_order_status(kwargs["id"], request.data["status"])
        return Response(status=status.HTTP_200_OK)

