import django_filters

from purchase.models import Purchase


class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = {
            'user_id': ['exact'],
            'book_id': ['exact'],
        }
