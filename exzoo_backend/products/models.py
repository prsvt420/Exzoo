from decimal import Decimal

from django.db import models
from django.db.models.expressions import Combinable

from products.enums import Unit


class Category(models.Model):
    objects: models.Manager = models.Manager()
    name: models.CharField = models.CharField(max_length=100)
    slug: models.SlugField = models.SlugField(max_length=100)

    class Meta:
        db_table: str = 'categories'
        db_table_comment: str = 'The table contains product categories'
        verbose_name_plural: str = 'categories'
        verbose_name: str = 'category'

    def __str__(self) -> str:
        """Return name of the category"""
        return self.name


class Tag(models.Model):
    objects: models.Manager = models.Manager()
    name: models.CharField = models.CharField(max_length=100)
    slug: models.SlugField = models.SlugField(max_length=100)

    class Meta:
        db_table: str = 'tags'
        db_table_comment: str = 'The table contains product tags'
        verbose_name_plural: str = 'tags'
        verbose_name: str = 'tag'

    def __str__(self) -> str:
        """Return name of the tag"""
        return str(self.name)


class Product(models.Model):
    objects: models.Manager = models.Manager()
    name: models.CharField = models.CharField(max_length=100)
    slug: models.SlugField = models.SlugField(max_length=100)
    description: models.TextField = models.TextField()
    image: models.ImageField = models.ImageField(upload_to='products', max_length=100)
    country_of_origin: models.CharField = models.CharField(max_length=100)
    price: models.DecimalField = models.DecimalField(max_digits=8, decimal_places=2)
    discount: models.DecimalField = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    unit: models.CharField = models.CharField(max_length=2, choices=Unit)
    quantity: models.PositiveIntegerField = models.PositiveIntegerField(default=0)
    category: models.ForeignKey[Category | Combinable, Category] = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE
    )
    tags: models.ManyToManyField = models.ManyToManyField(to='Tag', blank=True)

    class Meta:
        db_table: str = 'products'
        db_table_comment: str = 'The table contains products'
        verbose_name_plural: str = 'products'
        verbose_name: str = 'product'
        ordering: tuple[str] = ('id',)

    def __str__(self) -> str:
        """Return name of the product"""
        return str(self.name)

    def get_price(self) -> Decimal:
        """
        Return price of the product

        Returns:
            Decimal: Price of the product including discount
        """
        if self.discount:
            return Decimal(round(self.price - self.price * self.discount / 100, 2))
        return Decimal(self.price)
