from typing import List

from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view: type = get_schema_view(
    openapi.Info(
        title='Exzoo',
        default_version='v1',
        description='Exzoo Backend API',
        license=openapi.License(name='MIT License'),
    ),
)
urlpatterns: List[path] = [
    path(r'api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
