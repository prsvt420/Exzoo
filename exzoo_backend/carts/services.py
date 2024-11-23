from decimal import Decimal

from django.db.models import QuerySet

from carts.dataclasses import CartItemData
from carts.models import Cart
from products.models import Product
from users.models import User


class CartService:
    @staticmethod
    def get_cart_by_user(user: User) -> QuerySet[Cart]:
        """
        Get cart

        Returns:
            QuerySet[Cart]:
        """
        return Cart.objects.select_related('product').filter(user=user)

    @staticmethod
    def get_total_price_cart(user: User) -> Decimal:
        """
        Return total price of the cart

        Args:
            user: User:

        Returns:
            Decimal: total price of the cart
        """

        return Decimal(sum(cart.get_products_price() for cart in CartService.get_cart_by_user(user)))

    @staticmethod
    def add_to_cart(cart_data: CartItemData) -> Cart:
        """
        Add product to cart

        Args:
            cart_data: CartData

        Returns:
            Cart:
        """
        return Cart.objects.create(
            user=cart_data.user,
            product=cart_data.product,
            quantity=cart_data.quantity
        )

    @staticmethod
    def is_product_in_cart(user: User, product: Product) -> bool:
        """
        Check if product already in cart

        Args:
            user: User
            product: Product

        Returns:
            bool:
        """
        return Cart.objects.filter(user=user, product=product).exists()
