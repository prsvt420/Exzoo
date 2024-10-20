from django.db.models import QuerySet
from rest_framework import viewsets

from products.filters import ProductFilter
from products.models import Category, Product, Tag
from products.paginations import ProductPagination
from products.serializers import ProductSerializer, CategorySerializer, TagSerializer
from products.services import ProductService, CategoryService, TagService


class ProductViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Product] = ProductService.get_products()
    serializer_class: ProductSerializer = ProductSerializer
    pagination_class: ProductPagination = ProductPagination
    filterset_class: ProductFilter = ProductFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Category] = CategoryService.get_categories()
    serializer_class: CategorySerializer = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Tag] = TagService.get_tags()
    serializer_class: TagSerializer = TagSerializer
