from django.shortcuts import render

def MarketCloud(request):
    return render(request, 'marketcloud/shop.html')

def Product(request, slug):
    return render(request, 'marketcloud/product.html')
