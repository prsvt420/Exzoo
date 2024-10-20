from typing import List

from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import *

api_router: DefaultRouter = DefaultRouter()

api_router.register(prefix=r'products', viewset=ProductViewSet, basename='products')
api_router.register(prefix=r'categories', viewset=CategoryViewSet, basename='categories')
api_router.register(prefix=r'tags', viewset=TagViewSet, basename='tags')

urlpatterns: List[path] = [
    path('admin/', admin.site.urls),
    path('api/', include(arg=api_router.urls)),
    path('api/auth/', include(arg='djoser.urls')),
    path('api/auth/', include(arg='djoser.urls.authtoken')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += debug_toolbar_urls()
