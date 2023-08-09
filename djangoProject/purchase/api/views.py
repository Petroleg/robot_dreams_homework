import django_filters
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from purchase.api.filters import PurchaseFilter
from purchase.api.serializers import PurchaseSerializer
from purchase.models import Purchase


class PurchaseModelViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filterset_class = PurchaseFilter
    search_fields = ('id', 'user_id')
    ordering_fields = ('id',)
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
