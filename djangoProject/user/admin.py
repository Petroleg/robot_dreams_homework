from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from user.models import User


@admin.register(get_user_model())
class UserAdmin(UserAdmin):
    list_display = [
        User.__str__, 'id','password',
        'last_login', 'is_superuser', 'username',
        'email', 'is_staff', 'is_active',
        'date_joined', 'first_name', 'last_name', 'age'

    ]
    ordering = ['id']
    empty_value_display = "No data"
