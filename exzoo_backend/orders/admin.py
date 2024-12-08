from typing import Tuple, Any

from django.contrib import admin

from orders.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model: type[Any] = OrderItem
    extra: int = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display: Tuple = ('user', 'status', 'created_at')
    inlines: Tuple = (OrderItemInline,)
    list_filter: Tuple = ('status',)
    list_editable: Tuple = ('status',)
    list_per_page: int = 20


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display: Tuple = ('order', 'product', 'quantity')
    list_filter: Tuple = ('order',)
    list_per_page: int = 20
