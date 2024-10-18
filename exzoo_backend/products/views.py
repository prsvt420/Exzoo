from typing import Optional

from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from products.models import Category, Product, Tag
from products.serializers import ProductSerializer, CategorySerializer, TagSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    class ProductPagination(PageNumberPagination):
        page_size: int = 4
        page_query_param: str = 'page'

    serializer_class: ProductSerializer = ProductSerializer
    pagination_class: ProductPagination = ProductPagination
    lookup_field: str = 'slug'

    def get_queryset(self, *args, **kwargs) -> QuerySet[Product]:
        """
        Filter products by tag and category

        Returns:
            QuerySet[Product]: Filtered queryset
        """

        tags: Optional[list[str]] = self.request.query_params.getlist('tag')
        category_slug: Optional[str] = self.request.query_params.get('category')

        queryset: QuerySet[Product] = Product.objects.select_related('category').prefetch_related('tags').all()

        if tags:
            queryset = queryset.filter(tags__slug__in=tags)

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        return queryset


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset: QuerySet[Category] = Category.objects.all()
    serializer_class: CategorySerializer = CategorySerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset: QuerySet[Tag] = Tag.objects.all()
    serializer_class: TagSerializer = TagSerializer
