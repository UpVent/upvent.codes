from django.shortcuts import render

from .models import Product

def MarketCloud(request):

    products = Product.objects.filter(status=1).order_by("created_on")


    context = {
        'products': products
    }

    return render(request, 'marketcloud/shop.html', context)

def Item(request, slug):

    products = Product.objects.get(slug=slug)

    context = {
        'products': products
    }

    return render(request, 'marketcloud/product.html', context)
