from django_filters import rest_framework as filters

from products.models import Product
from products.services import TagService, CategoryService


class ProductFilter(filters.FilterSet):
    category: filters.ModelChoiceFilter = filters.ModelChoiceFilter(
        queryset=CategoryService.get_categories(),
        to_field_name='slug'

    )
    tags: filters.ModelMultipleChoiceFilter = filters.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        queryset=TagService.get_tags(),
        to_field_name='slug'
    )

    class Meta:
        model: type[Product] = Product
        fields: tuple = ('category', 'tags')
