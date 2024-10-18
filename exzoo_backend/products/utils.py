from django_filters import rest_framework as filters

from products.models import Product, Tag, Category


class ProductFilter(filters.FilterSet):
    category: filters.ModelChoiceFilter = filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        to_field_name='slug'

    )
    tags: filters.ModelMultipleChoiceFilter = filters.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        queryset=Tag.objects.all(),
        to_field_name='slug'
    )

    class Meta:
        model: Product = Product
        fields: tuple = ('category', 'tags')
