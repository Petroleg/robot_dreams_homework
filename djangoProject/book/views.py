from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import BookForm
from .models import Book


class BookListView(ListView):
    template_name = 'book/book_list.html'
    model = Book


class BookDetailView(DetailView):
    template_name = 'book/book_detail.html'
    model = Book


class BookCreateView(CreateView):
    model = Book
    template_name = 'user/user_create.html'
    form_class = BookForm
    success_url = reverse_lazy('books:books-all')
