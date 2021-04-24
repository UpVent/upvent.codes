from django.shortcuts import render

from .models import Project, FSProject, PrivacyPolicy

# Create your views here.
def index(request):
    """
    Display the main page for this site.

    **Context**

    ``index``
        A single array with a 1 value, meant to be used for something else.

    **Template:**

    :template:`core/index.html`

    """

    index = ['01']
    return render(request, 'core/index.html', {'index': index})

def about(request):

    """
    Display the "about" page for this site.

    **Context**

    ``projects``
        All instances of the :model:`core.Project` saved in the database

    **Template**
        :template:`core/about.html`

    """

    projects = Project.objects.all()
    return render(request, 'core/about.html', {'projects': projects})

def services(request):

    """
    Display the "services" page for this site.

    **Context**

    ``services``
        All instances of the :model:`core.FSProject` saved in the database

    **Template**
        :template:`core/services.html`

    """

    services = FSProject.objects.all()
    return render(request, 'core/services.html', {'services': services})

def licenses(request):
    return render(request, 'core/licenses.html')

def privacy_policy(request):

    """
    Display the "privacy-policy" page for this site.

    **Context**

    ``policies``
        Return the only instance of the :model:`core.PrivacyPolicy`
        saved in the database. This model allows ONLY ONE privacy policy.

    **Template**
        :template:`core/privacy-policy.html`

    """

    policies = PrivacyPolicy.objects.all().first()
    return render(request, 'core/privacy-policy.html', {'policies': policies})
