from django.urls import path

from user import views

app_name = 'users'

urlpatterns = [
    path('', views.UserListView.as_view(), name='users-all'),
    path('<int:pk>', views.UserDetailView.as_view(), name='users-detail'),
    path('create', views.UserCreateView.as_view(), name='users-create'),
]
