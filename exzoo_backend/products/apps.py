from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'products'
