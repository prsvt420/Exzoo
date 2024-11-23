from django.contrib import admin

from carts.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    fields: tuple = ('user', ('product', 'quantity'))
    list_display: tuple = ('user', 'product', 'quantity', 'products_price')
    list_filter: tuple = ('user', 'product')
    search_fields: tuple = ('user', 'product')
    list_editable: tuple = ('quantity',)
    list_per_page: int = 25

    @staticmethod
    def products_price(obj: Cart):
        return obj.get_products_price()
