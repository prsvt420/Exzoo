from decimal import Decimal
from typing import Optional

from django.db import models


class Product(models.Model):
    objects: Optional[models.Manager] = None

    class Unit(models.TextChoices):
        KILOGRAM = 'KG', 'kilogram'
        PIECE = 'PC', 'piece'

    name: str = models.CharField(max_length=100)
    slug: str = models.SlugField(max_length=100)
    description: str = models.TextField()
    image: str = models.ImageField(upload_to='products', max_length=100)
    country_of_origin: str = models.CharField(max_length=100)
    price: Decimal = models.DecimalField(max_digits=8, decimal_places=2)
    discount_price: Decimal = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    unit: models.CharField = models.CharField(max_length=2, choices=Unit)
    quantity = models.PositiveIntegerField(default=0)
    category: models.ForeignKey = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    tags: models.ManyToManyField = models.ManyToManyField(to='Tag', blank=True)

    class Meta:
        db_table: str = 'products'
        db_table_comment: str = 'The table contains products'
        verbose_name_plural: str = 'products'
        verbose_name: str = 'product'

    def __str__(self) -> str:
        """Return name of the product"""
        return self.name

    def get_price(self) -> Decimal:
        """
        Return price of the product

        Returns:
            Decimal: Price of the product including discount
        """
        if self.discount_price:
            return round(self.price - self.price * self.discount_price / 100, 2)
        return self.price


class Category(models.Model):
    objects: Optional[models.Manager] = None
    name: str = models.CharField(max_length=100)
    slug: str = models.SlugField(max_length=100)

    class Meta:
        db_table: str = 'categories'
        db_table_comment: str = 'The table contains product categories'
        verbose_name_plural: str = 'categories'
        verbose_name: str = 'category'

    def __str__(self) -> str:
        """Return name of the category"""
        return self.name


class Tag(models.Model):
    objects: Optional[models.Manager] = None
    name: str = models.CharField(max_length=100)
    slug: str = models.SlugField(max_length=100)

    class Meta:
        db_table: str = 'tags'
        db_table_comment: str = 'The table contains product tags'
        verbose_name_plural: str = 'tags'
        verbose_name: str = 'tag'

    def __str__(self) -> str:
        """Return name of the tag"""
        return self.name
