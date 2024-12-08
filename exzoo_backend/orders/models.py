from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models

from orders.choices import StatusChoices
from products.models import Product
from users.models import User


class Order(models.Model):
    user: User = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    status: str = models.CharField(
        choices=StatusChoices.choices,
        default=StatusChoices.PROCESSING, max_length=2
    )
    address: str = models.CharField(max_length=255)
    is_paid: bool = models.BooleanField(default=False)
    phone_number: str = models.CharField(max_length=20)

    class Meta:
        db_table: str = 'orders'
        db_table_comment: str = 'The table contains orders'
        verbose_name_plural: str = 'orders'
        verbose_name: str = 'order'

    def __str__(self) -> str:
        return f'[order {self.user} {self.created_at}] {self.get_status_display()}'

    def get_total_price(self) -> Decimal:
        return Decimal(sum(item.price * item.quantity for item in self.items.all().select_related('product')))


class OrderItem(models.Model):
    order: Order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product: Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity: int = models.PositiveIntegerField(default=1)
    price: Decimal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table: str = 'order_items'
        db_table_comment: str = 'The table contains order items'
        verbose_name_plural: str = 'order items'
        verbose_name: str = 'order item'

    def __str__(self) -> str:
        return f'order item'