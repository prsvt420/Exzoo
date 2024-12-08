from decimal import Decimal

from django.db.models import QuerySet

from carts.models import Cart
from orders.models import Order
from users.models import User


class OrderService:
    @staticmethod
    def get_user_orders(user: User) -> QuerySet[Order]:
        """
        Get user orders

        Args:
            user: User

        Returns:
            QuerySet[Order]:
        """

        return Order.objects.filter(user=user).select_related('user')

    @staticmethod
    def create_order(carts: QuerySet[Cart], user: User) -> Order:
        """
        Create order

        Args:
            carts: QuerySet[Cart]
            user: User

        Returns:
            Order:
        """

        order: Order = Order.objects.create(user=user)

        for cart in carts:
            order.items.create(
                product=cart.product,
                quantity=cart.quantity,
                price=cart.product.price
            )

        return order
