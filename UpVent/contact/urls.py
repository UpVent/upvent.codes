from . import views
from .views import contact
from django.urls import path


app_name = 'contact'

urlpatterns = [
    path('', contact, name='home'),
]
