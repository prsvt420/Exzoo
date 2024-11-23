from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product
from users.models import User


class Cart(models.Model):
    user: User = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product: Product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity: int = models.PositiveIntegerField(default=1)

    class Meta:
        db_table: str = 'carts'
        db_table_comment: str = 'The table contains carts'
        verbose_name_plural: str = 'carts'
        verbose_name: str = 'cart'
        unique_together: tuple = ('user', 'product')

    def __str__(self) -> str:
        return f'[cart {self.user}] {self.product}'

    def get_products_price(self) -> Decimal:
        """
        Return products price

        Returns:
            Decimal: products price
        """
        return Decimal(round(self.product.get_price() * self.quantity, 2))
