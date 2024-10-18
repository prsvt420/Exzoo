from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from products.models import Category, Product, Tag
from products.serializers import ProductSerializer, CategorySerializer, TagSerializer
from products.utils import ProductFilter


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    class ProductPagination(PageNumberPagination):
        page_size: int = 4
        page_query_param: str = 'page'

    queryset: QuerySet[Product] = Product.objects.select_related('category').prefetch_related('tags').all()
    serializer_class: ProductSerializer = ProductSerializer
    pagination_class: ProductPagination = ProductPagination
    filterset_class: ProductFilter = ProductFilter


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset: QuerySet[Category] = Category.objects.all()
    serializer_class: CategorySerializer = CategorySerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset: QuerySet[Tag] = Tag.objects.all()
    serializer_class: TagSerializer = TagSerializer
