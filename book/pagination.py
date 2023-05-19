from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    page_size = 10


class DefaultBookPagination(PageNumberPagination):
    page_size = 50
