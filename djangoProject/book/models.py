from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.SmallIntegerField(null=True)
    price = models.SmallIntegerField(null=True)

    class Meta:
        db_table = 'book'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_title_author'
            )
        ]
