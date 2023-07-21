from django.shortcuts import render
from django.http import JsonResponse


from purchase.models import Purchase


def purchases(request):
    purchases_qs = Purchase.objects.values()
    data = list(purchases_qs)
    return JsonResponse(data, safe=False, status=200)
