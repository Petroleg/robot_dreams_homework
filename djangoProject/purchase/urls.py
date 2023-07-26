from django.urls import path

from purchase import views

app_name = 'purchases'

urlpatterns = [
    path('', views.PurchaseListView.as_view(), name='purchases-all'),
    path('<int:pk>', views.PurchaseDetailView.as_view(), name='purchases-detail'),
    path('<create>', views.PurchaseCreateView.as_view(), name='purchases-create'),
]
