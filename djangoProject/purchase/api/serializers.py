from rest_framework import serializers

from purchase.models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('id', 'book_id', 'user_id', 'date')
