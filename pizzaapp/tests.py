from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from django.urls import reverse
import datetime
import random

from .models import Customer, Order, OrderStatus, Pizza, PizzaIngredient, Ingredient

client = APIClient()


class InsertAndGetOrders(APITestCase):
    customer = Customer

    def setUp(self):
        self.populate_db()

    def test_get_all_orders(self):
        order_count = 3

        for count in range(order_count):
            self.create_order(self.customer)

        url = reverse('get-all-orders')
        response = self.client.get(url, {}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), order_count)

    def populate_db(self):
        self.create_customer()
        self.create_ingredients()
        self.create_orderstatus()

    def create_order(self, customer):
        order = Order.objects.create(
            status=OrderStatus.objects.filter(label='Placed').first(),
            customer=customer,
            total_price=random.uniform(5.00, 20.00),
            placed_datetime=datetime.datetime.now()
        )
        self.create_pizza(order)

    def create_pizza(self, order):
        pizza = Pizza.objects.create(
            order=order,
            quantity=1,
            size="M",
            price=5.95
        )

    def create_customer(self):
        self.customer = Customer.objects.create(
            first_name='test',
            last_name='customer',
            address='123 Test Street, Berlin DE',
            phone_number='+49 123 4567890'
        )

    def create_ingredients(self):
        Ingredient.objects.create(
            display_name='Pepperoni',
            code='PEPPERONI',
            price=1.00
        )
        Ingredient.objects.create(
            display_name='White Onion',
            code='ONION',
            price=0.25
        )
        Ingredient.objects.create(
            display_name='Green Pepper',
            code='GREENPEP',
            price=0.50
        )
        Ingredient.objects.create(
            display_name='Red Tomato',
            code='TOMATO',
            price=0.75
        )

    def create_orderstatus(self):
        OrderStatus.objects.create(
            label='Placed'
        )
        OrderStatus.objects.create(
            label='Processing'
        )
        OrderStatus.objects.create(
            label='Ready'
        )

