from django.contrib import admin

from purchase.models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = [Purchase.__str__, 'id', 'user_id', 'book_id', 'date']
    ordering = ['id']
    empty_value_display = "No data"
