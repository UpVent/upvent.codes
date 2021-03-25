from . import views
from django.urls import path
from .views import Blog, BlogEntry

app_name = 'blog'

urlpatterns = [
    path('', Blog, name='home'),
    path('<slug:slug>/', BlogEntry, name='post')
]
