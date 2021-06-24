from django.urls import path
from django.conf import settings
from .views import Library

app_name = 'education'

from . import views

urlpatterns = [
    path('', Library, name='home'),
    # path('<slug:slug>/', BlogEntry, name='post')
]
