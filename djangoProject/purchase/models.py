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
        verbose_name = 'My purchase'
        verbose_name_plural = 'My purchases'

    def __str__(self):
        return f'Purchase with id {self.id}, user id {self.user_id}, book id {self.book_id}, date {str(self.date)[0:-6]}'
