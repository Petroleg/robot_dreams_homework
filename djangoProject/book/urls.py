from django.urls import path

from book import views

app_name = 'books'

urlpatterns = [
    path('', views.BookListView.as_view(), name='books-all'),
    path('<int:pk>', views.BookDetailView.as_view(), name='books-detail'),
    path('<create>', views.BookCreateView.as_view(), name='books-create'),
]
