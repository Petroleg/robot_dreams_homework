from django.urls import path
from rest_framework.routers import SimpleRouter

from book import views
from book.api import views as api_views

app_name = 'books'

urlpatterns = [
    path('', views.BookListView.as_view(), name='books-all'),
    path('<int:pk>', views.BookDetailView.as_view(), name='books-detail'),
    path('<create>', views.BookCreateView.as_view(), name='books-create'),
]

router = SimpleRouter()
router.register('api', api_views.BookModelViewSet)

urlpatterns += router.urls
