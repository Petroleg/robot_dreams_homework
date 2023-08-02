import django_filters

from user.models import User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'username': ['exact'],
            'age': ['gte'],
        }
