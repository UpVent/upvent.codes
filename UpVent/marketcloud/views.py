import stripe

from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View


def MarketCloud(request):
    return render(request, 'marketcloud/shop.html')

def Product(request, slug):
    return render(request, 'marketcloud/product.html')
