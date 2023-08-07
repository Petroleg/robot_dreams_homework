from django.urls import path
from rest_framework.routers import SimpleRouter

from purchase import views
from purchase.api import views as api_views

app_name = 'purchases'

urlpatterns = [
    path('', views.PurchaseListView.as_view(), name='purchases-all'),
    path('<int:pk>', views.PurchaseDetailView.as_view(), name='purchases-detail'),
    path('<create>', views.PurchaseCreateView.as_view(), name='purchases-create'),
]

router = SimpleRouter()
router.register('api', api_views.PurchaseModelViewSet)

urlpatterns += router.urls
