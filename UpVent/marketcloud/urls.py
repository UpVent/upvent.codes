from . import views
from django.urls import path
from .views import MarketCloud, Product

app_name = 'marketcloud'

urlpatterns = [
    path('', MarketCloud, name='home'),
    path('<slug:slug>/', Product, name='post')
]
