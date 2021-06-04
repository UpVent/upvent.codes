from . import views
from django.urls import path
from .views import MarketCloud, Item

app_name = 'marketcloud'

urlpatterns = [
    path('', MarketCloud, name='home'),
    path('<slug:slug>/', Item, name='item')
]
