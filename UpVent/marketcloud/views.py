from django.shortcuts import render

# Create your views here.

def MarketCloud(request):
    return render(request, 'marketcloud/shop.html', {})

def Product(request, slug):
    return render(request, 'marketcloud/product.html', {})
