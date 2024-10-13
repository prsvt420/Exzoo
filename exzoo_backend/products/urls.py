from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import ProductViewSet, CategoryViewSet, TagViewSet

router: DefaultRouter = DefaultRouter()

router.register(prefix=r'products', viewset=ProductViewSet, basename='products')
router.register(prefix=r'categories', viewset=CategoryViewSet, basename='categories')
router.register(prefix=r'tags', viewset=TagViewSet, basename='tags')

app_name: str = 'products'

urlpatterns: list[path] = [
    path('', include(router.urls)),
]
