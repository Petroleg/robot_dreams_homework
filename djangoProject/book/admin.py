from django.contrib import admin


from book.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [Book.__str__, 'id', 'title', 'author', 'year', 'price']
    ordering = ['id']
    empty_value_display = "No data"
    pass