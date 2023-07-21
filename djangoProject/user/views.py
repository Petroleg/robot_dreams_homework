from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from user.models import User


def users(request):
    users = User.objects.values()
    data = list(users)
    return JsonResponse({'data': data})


def users(request):
    users = User.objects.values()
    data = list(users)
    return JsonResponse(data, safe=False, status=200)


def users(request):
    qs = User.objects.all()
    qs_json = serializers.serialize('json', qs)
    return HttpResponse(qs_json, content_type='application/json')
