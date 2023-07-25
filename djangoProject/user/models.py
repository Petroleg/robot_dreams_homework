from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(null=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'My user'
        verbose_name_plural = 'My users'

    def __str__(self):
        return f"User {self.username} named {self.first_name} {self.last_name}, {self.age} years old. Id: {self.id}"
