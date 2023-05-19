from django_filters.rest_framework import FilterSet

from book.models import Author


class AuthorFilter(FilterSet):
    class Meta:
        model = Author
        fields= ['name', 'date_of_birth']