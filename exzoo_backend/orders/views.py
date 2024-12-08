from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from orders.models import Order
from orders.serializers import OrderSerializer
from orders.services import OrderService


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class: OrderSerializer = OrderSerializer
    permission_classes: tuple = (IsAuthenticated,)

    def get_queryset(self) -> QuerySet[Order]:
        return OrderService.get_user_orders(self.request.user)
