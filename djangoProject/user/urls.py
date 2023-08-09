from django.urls import path
from rest_framework.routers import SimpleRouter

from user import views
from user.api import views as api_views


app_name = 'users'

urlpatterns = [
    path('', views.UserListView.as_view(), name='users-all'),
    path('<int:pk>', views.UserDetailView.as_view(), name='users-detail'),
    path('create', views.UserCreateView.as_view(), name='users-create'),
]

router = SimpleRouter()
router.register('api', api_views.UserModelViewSet)

urlpatterns += router.urls
