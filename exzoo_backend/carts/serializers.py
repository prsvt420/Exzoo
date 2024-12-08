from decimal import Decimal

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from carts.dataclasses import CartItemData
from carts.models import Cart
from carts.services import CartService
from products.models import Product
from products.services import ProductService
from users.models import User


class CartSerializer(serializers.ModelSerializer):
    products_price: serializers.SerializerMethodField = serializers.SerializerMethodField()
    quantity: serializers.IntegerField = serializers.IntegerField(min_value=1, required=False)
    product: serializers.PrimaryKeyRelatedField = serializers.PrimaryKeyRelatedField(
        queryset=ProductService.get_products()
    )

    class Meta:
        model: type[Cart] = Cart
        fields: tuple = ('id', 'product', 'quantity', 'products_price')

    def validate(self, attrs: dict) -> dict:
        """
        Check if product already in cart

        Args:
            attrs: dict

        Returns:
            dict:
        """

        user: User = self.context['request'].user
        product: Product = attrs['product']

        if CartService.is_product_in_cart(user, product):
            raise ValidationError('Product already in cart')

        return attrs

    def create(self, validated_data: dict) -> Cart:
        """
        Add product to cart

        Args:
            validated_data: dict

        Returns:
            Cart:
        """

        validated_data['user'] = self.context['request'].user
        validated_data['product'] = ProductService.get_product_by_id(validated_data['product'].id)
        cart_data: CartItemData = CartItemData(**validated_data)

        return CartService.add_to_cart(cart_data)

    @staticmethod
    def get_products_price(cart: Cart) -> Decimal:
        """
        Return products price

        Args:
            cart: Cart

        Returns:
            Decimal:
        """

        return cart.get_products_price()

    def to_representation(self, instance: Cart) -> dict:
        """
        Return cart representation

        Args:
            instance: Cart

        Returns:
            dict:
        """
        representation: dict = super().to_representation(instance)
        product: Product = instance.product

        representation['product'] = {
            'id': product.pk,
            'name': product.name,
            'price': product.price,
            'slug': product.slug
        }

        return representation
