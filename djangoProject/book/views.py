from django.shortcuts import render
from django.http import JsonResponse


from book.models import Book


def books(request):
    books_qs = Book.objects.values()
    data = list(books_qs)
    return JsonResponse(data, safe=False, status=200)
