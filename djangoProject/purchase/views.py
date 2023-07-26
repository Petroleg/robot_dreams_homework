from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import PurchaseForm
from .models import Purchase


class PurchaseListView(ListView):
    template_name = "purchase/purchase_list.html"
    model = Purchase


class PurchaseDetailView(DetailView):
    template_name = "purchase/purchase_detail.html"
    model = Purchase


class PurchaseCreateView(CreateView):
    model = Purchase
    template_name = 'purchase/purchase_create.html'
    form_class = PurchaseForm
    success_url = reverse_lazy('purchases:purchases-all')
