from decimal import Decimal
from typing import Any

from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer

from carts.models import Cart
from carts.serializers import CartSerializer
from carts.services import CartService


class CartViewSet(viewsets.ModelViewSet):
    serializer_class: type[BaseSerializer[Any]] | None = CartSerializer
    permission_classes: tuple = (IsAuthenticated,)

    def get_queryset(self) -> QuerySet[Cart]:
        """
        Get user cart

        Returns:
            QuerySet[Cart]:
        """

        return CartService.get_cart_by_user(self.request.user)

    def list(self, request: Request, *args, **kwargs) -> Response:
        """
        Get user cart

        Args:
            request: Response
            *args:
            **kwargs:

        Returns:
            Response:
        """
        queryset: QuerySet[Cart] = self.get_queryset()
        serializer: BaseSerializer[Any] = self.get_serializer(queryset, many=True)
        total_price_cart: Decimal = CartService.get_total_price_cart(self.request.user)

        response: Response = Response({
            'cart_items': serializer.data,
            'total_price_cart': total_price_cart
        })

        return response
