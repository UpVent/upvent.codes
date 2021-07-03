from django.urls import path
from django.conf import settings
from .views import Library, ResView

app_name = 'education'

from . import views

urlpatterns = [
    path('', Library, name='home'),
    path('<slug:slug>/', ResView, name='resource')
]
