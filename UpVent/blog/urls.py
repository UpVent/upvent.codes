from django.urls import path
from .views import Blog, BlogEntry, BlogSearch

app_name = 'blog'

urlpatterns = [
    path('', Blog, name='home'),
    path('entry/<slug>/', BlogEntry, name='post'),
    path('search/', BlogSearch, name='blog-search'),
]
