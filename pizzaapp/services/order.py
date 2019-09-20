from ..models import Order, OrderStatus, Customer, Ingredient, PizzaIngredient, Pizza

import random, datetime


class OrderService:
    # Retrieve all orders, with optional filters.
    @staticmethod
    def get_all_orders(customer_id=None, status_id=None):
        orders = Order.objects.all()

        if customer_id is not None:
            existing_customer = Customer.objects.filter(pk=customer_id).first()
            if existing_customer is not None:
                orders = orders.filter(customer=existing_customer)

        if status_id is not None:
            order_status = OrderStatus.objects.filter(pk=status_id).first()
            if order_status is not None:
                orders = orders.filter(status=order_status)

        return orders

    # Create new order, with associated pizzas.
    @staticmethod
    def place_order(order: Order):
        try:
            # Create Order
            total_price = random.uniform(5.00, 50.00)
            order_status = OrderStatus.objects.filter(label='Placed').first()
            placed_datetime = datetime.datetime.now()
            customer = Customer.objects.get(id=order['customer'])

            new_order = Order.objects.create(
                total_price=total_price,
                status=order_status,
                placed_datetime=placed_datetime,
                customer=customer
            )
            OrderService.create_pizzas(new_order, order['pizzas'])

            return new_order
        except Exception as e:
            raise ValueError("Something went wrong creating orders.")

    # update an existing order
    @staticmethod
    def update_order(order_id, order: Order):
        existing_order = Order.objects.get(pk=order_id)

        if existing_order.status.label != 'Placed' and existing_order.status.label != 'Processing':
            raise ValueError("Cannot modify completed or cancelled order.")
        else:
            Pizza.objects.filter(order=existing_order).delete()
            OrderService.create_pizzas(existing_order, order['pizzas'])

        return existing_order

    @staticmethod
    def delete_order(order_id):
        existing_order = Order.objects.get(pk=order_id)

        if existing_order.status.label != 'Placed' and existing_order.status.label != 'Processing':
            raise ValueError("Cannot cancel an order that has been processed or cancelled.")
        else:
            existing_order.delete()
            return str("Successfully cancelled order with id " + order_id)

    # create pizzas associated to orders
    @staticmethod
    def create_pizzas(order: Order, pizzas):
        try:
            # Create Pizzas
            for pizza in pizzas:
                new_pizza = Pizza.objects.create(
                    order=order,
                    quantity=pizza['quantity'],
                    size=pizza['size'],
                    price=random.uniform(5.00, 10.00)
                )

                # Create Pizza Ingredients relationship
                for pizza_ingredient in pizza['ingredients']:
                    stock_ingredient = Ingredient.objects.filter(code=pizza_ingredient).first()
                    PizzaIngredient.objects.create(
                        pizza=new_pizza,
                        ingredient=stock_ingredient
                    )
        except Exception as e:
            raise ValueError("Something went wrong creating pizzas.")


    @staticmethod
    def update_order_status(order_id, status_id):
        order = Order.objects.filter(pk=order_id).update(status=status_id)

