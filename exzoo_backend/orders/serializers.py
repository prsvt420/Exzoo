from decimal import Decimal
from typing import Tuple

from django.db.models import QuerySet
from rest_framework import serializers

from carts.models import Cart
from carts.services import CartService
from orders.models import Order, OrderItem
from orders.services import OrderService
from users.models import User


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model: OrderItem = OrderItem
        fields: Tuple = ('id', 'product', 'quantity')

    def to_representation(self, instance: OrderItem) -> dict:
        """
        Return order item representation

        Args:
            instance: OrderItem

        Returns:
            dict:
        """
        representation = super().to_representation(instance)
        representation['product'] = instance.product.name
        representation['slug'] = instance.product.slug
        representation['price'] = instance.product.price
        return representation


class OrderSerializer(serializers.ModelSerializer):
    items: OrderItemSerializer = OrderItemSerializer(many=True, read_only=True)
    total_price_order: Decimal = serializers.SerializerMethodField()

    class Meta:
        model: Order = Order
        fields: Tuple = ('id', 'user', 'status', 'created_at', 'items', 'total_price_order')
        read_only_fields: Tuple = ('user', 'status')

    def create(self, validated_data: dict) -> Order:
        """
        Create order

        Args:
            validated_data: dict

        Returns:
            Order:
        """
        user: User = self.context['request'].user
        carts: QuerySet[Cart] = CartService.get_cart_by_user(user)

        if not carts:
            raise serializers.ValidationError('Cart is empty')

        order = OrderService.create_order(carts, user)
        CartService.clear_user_cart(user)
        return order

    @staticmethod
    def get_total_price_order(order: Order) -> Decimal:
        """
        Return total price order

        Args:
            order: Order

        Returns:
            Decimal:
        """
        return order.get_total_price()
