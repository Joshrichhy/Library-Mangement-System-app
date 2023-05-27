from django_filters.rest_framework import FilterSet

from book.models import Author, Book


class AuthorFilter(FilterSet):
    class Meta:
        model = Author
        fields = ['name', 'date_of_birth']
        # the fields can also be made as a dictionary
        # fields = {
        #     'name': ['exact']
        # }


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['exact'],
            'price': ['gt', 'lt']
            #gt is greater than, lt is less than, works with range

        }
