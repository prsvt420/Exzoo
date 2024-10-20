from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size: int = 4
    page_query_param: str = 'page'
