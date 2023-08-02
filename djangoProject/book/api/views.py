import django_filters
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from book.api.filters import BookFilter
from book.api.serializers import BookSerializer
from book.models import Book


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    search_fields = ('id', 'title')
    ordering_fields = ('id',)
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
