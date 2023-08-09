import django_filters

from book.models import Book


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['exact'],
            'price': ['lte'],
        }
