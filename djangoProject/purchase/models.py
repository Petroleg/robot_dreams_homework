from django.db import models

from book.models import Book
from user.models import User


from django.utils import timezone


class Purchase(models.Model):
    user = models.ForeignKey(User, related_name='purchases', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='books', on_delete=models.CASCADE)
    date = models.DateTimeField(null=True)

    class Meta:
        db_table = 'purchase'
        ordering = ["-date"]
