from typing import Any

from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.pagination import BasePagination
from rest_framework.serializers import BaseSerializer

from products.filters import ProductFilter
from products.models import Category, Product, Tag
from products.paginations import ProductPagination
from products.serializers import ProductSerializer, CategorySerializer, TagSerializer
from products.services import ProductService, CategoryService, TagService


class ProductViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Product] = ProductService.get_products()
    serializer_class: type[BaseSerializer[Any]] = ProductSerializer
    pagination_class: type[BasePagination] | None = ProductPagination
    filterset_class: type[ProductFilter] = ProductFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Category] = CategoryService.get_categories()
    serializer_class: type[BaseSerializer[Any]] | None = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Tag] = TagService.get_tags()
    serializer_class: type[BaseSerializer[Any]] | None = TagSerializer
