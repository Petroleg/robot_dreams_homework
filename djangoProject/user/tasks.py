from celery import shared_task

from user.models import User
from purchase.models import Purchase


@shared_task
def print_hello_world():
    print("Hello World from task")


@shared_task
def print_purchases(user_id):
    purchases = Purchase.objects.filter(user_id=user_id).count()
    print(purchases)


@shared_task
def each_minute_print():
    print(User.objects.count())
