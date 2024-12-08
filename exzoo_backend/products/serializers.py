from decimal import Decimal

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from products.models import Product, Category, Tag


class CategorySerializer(ModelSerializer):
    class Meta:
        model: type[Category] = Category
        fields: str = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model: type[Tag] = Tag
        fields: str = '__all__'


class ProductSerializer(ModelSerializer):
    category: CategorySerializer = CategorySerializer(read_only=True)
    tags: TagSerializer = TagSerializer(many=True, read_only=True)
    price: serializers.SerializerMethodField = serializers.SerializerMethodField()

    class Meta:
        model: type[Product] = Product
        fields: tuple = (
            'id',
            'name',
            'slug',
            'description',
            'image',
            'country_of_origin',
            'price',
            'discount',
            'unit',
            'quantity',
            'category',
            'tags'
        )

    @staticmethod
    def get_price(obj: Product) -> Decimal:
        """
        Return price of the product

        Parameters:
            obj(Product): Product

        Returns:
            Decimal: Price of the product
        """
        return obj.get_price()
