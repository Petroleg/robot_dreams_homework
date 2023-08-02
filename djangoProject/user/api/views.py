import django_filters
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from user.api.filters import UserFilter
from user.api.pagination import CustomPagination
from user.api.serializers import UserSerializer
from user.models import User


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
    search_fields = ('id', 'username')
    ordering_fields = ('id',)
    pagination_class = CustomPagination
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
