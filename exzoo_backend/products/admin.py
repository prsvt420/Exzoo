from django.contrib import admin

from products.models import Product, Category, Tag


class BaseAdmin(admin.ModelAdmin):
    fields: tuple = ('name', 'slug',)
    list_display: tuple = ('name', 'slug')
    search_fields: tuple = ('name',)
    prepopulated_fields: dict = {'slug': ('name',)}
    list_per_page: int = 25


@admin.register(Product)
class ProductAdmin(BaseAdmin):
    fields: tuple = (
        ('name', 'slug'),
        ('description', 'country_of_origin'),
        ('price', 'unit', 'discount',),
        ('category', 'tags'),
        'image',
        'quantity',
    )
    list_display: tuple = ('name', 'price', 'discount', 'category', 'unit', 'quantity')
    search_fields: tuple = ('name', 'description', 'country_of_origin')
    list_filter: tuple = ('category', 'tags')
    filter_horizontal: tuple = ('tags',)
    list_editable: tuple = ('price', 'discount', 'unit', 'quantity')


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    ...


@admin.register(Tag)
class TagAdmin(BaseAdmin):
    ...
