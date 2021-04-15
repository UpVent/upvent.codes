from django.shortcuts import render

from .models import Project, PrivacyPolicy

# Create your views here.
def index(request):
    index = ['01']
    return render(request, 'core/index.html', {'index': index})

def about(request):
    projects = Project.objects.all()
    return render(request, 'core/about.html', {'projects': projects})

def services(request):
    return render(request, 'core/services.html')

def privacy_policy(request):
    priv_pol = PrivacyPolicy.objects.all()
    return render(request, 'core/privacy-policy.html', {'policy': priv_pol})
