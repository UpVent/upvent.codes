from django.shortcuts import render

from .models import Project, FSProject, PrivacyPolicy

# Create your views here.
def index(request):
    index = ['01']
    return render(request, 'core/index.html', {'index': index})

def about(request):
    projects = Project.objects.all()
    return render(request, 'core/about.html', {'projects': projects})

def services(request):
    services = FSProject.objects.all()
    return render(request, 'core/services.html', {'services': services})

def privacy_policy(request):
    policies = PrivacyPolicy.objects.all().first()
    return render(request, 'core/privacy-policy.html', {'policies': policies})
