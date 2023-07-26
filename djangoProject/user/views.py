from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import UserForm
from .models import User


class UserListView(ListView):
    template_name = "user/user_list.html"
    model = User


class UserDetailView(DetailView):
    template_name = "user/user_detail.html"
    model = User


class UserCreateView(CreateView):
    model = User
    template_name = 'user/user_create.html'
    form_class = UserForm
    success_url = reverse_lazy('users:users-all')
