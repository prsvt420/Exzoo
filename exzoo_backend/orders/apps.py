from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'orders'
