from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import CustomUserCreationForm
from .models import User
from .tasks import print_hello_world, print_purchases, each_minute_print


class UserListView(ListView):
    template_name = "user/user_list.html"
    model = User

    def get_context_data(self, **kwargs):
        print_hello_world.delay()
        return super().get_context_data(**kwargs)


class UserDetailView(DetailView):
    template_name = "user/user_detail.html"
    model = User

    def dispatch(self, request, *args, **kwargs):
        each_minute_print.delay()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.get_object()

        print_purchases.delay(user.id)

        return context


class UserCreateView(CreateView):
    model = User
    template_name = 'user/user_create.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:users-all')
