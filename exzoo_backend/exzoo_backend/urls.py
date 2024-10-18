from typing import List

from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns: List[path] = [
    path('admin/', admin.site.urls),
    path('api/', include(arg='products.urls', namespace='api_products'), name='api_products'),
    path('auth/', include(arg='djoser.urls'), name='auth'),
    re_path(r'^auth/', include(arg='djoser.urls.authtoken'), name='auth_token'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += debug_toolbar_urls()
