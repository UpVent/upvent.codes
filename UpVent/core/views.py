from django.shortcuts import render
from django.contrib import messages


from .models import (Testimonial,
                     Project,
                     FSProject,
                     License,
                     HOF,
                     TeamMember,
                     PrivacyPolicy)

# Create your views here.
def index(request):
    """
    Display the main page for this site.

    **Context**

    ``testimonials``
        All instances of the :model:`core.Testimonial` saved in the database.

    **Template:**

    :template:`core/index.html`

    """

    testimonials = Testimonial.objects.all()
    return render(request, 'core/index.html', {'testimonials': testimonials})

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

    """
    Display the "licenses" page for this site.

    **Context**

    ``licenses``
        Return all instances of the :model:`core.License`
        saved in the database to display in the first section of the page.

    ``HOF``
        Return all instances of recognized projects shown in the
        hall of fame at the last section of the page.

    **Template**
        :template:`core/licenses.html`
    """

    licenses = License.objects.all()
    hall_of_fame = HOF.objects.all()

    context = {
        'licenses': licenses,
        'hall_of_fame': hall_of_fame,
    }

    return render(request, 'core/licenses.html', context)

def team(request):
    """
    Display the "team" page for this site.

    **Context**

    ``members``
        Return all the members with the field is_collab marked as "False".

    ``collabs``
        Return all the members with the field is_collab marked as "True".

    **Template**
        :template:`core/team.html`
    """

    members = TeamMember.objects.filter(is_collab = False)
    collabs = TeamMember.objects.filter(is_collab = True)

    context = {
        'members': members,
        'collabs': collabs,
    }

    return render(request, 'core/team.html', context)

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

# Search field related
def search(request):

    from blog.models import Post

    query = request.GET['search']

    if len(query) > 80:
        all_posts = Post.objects.none()
    else:
        all_testimonials = Testimonial.objects.filter(name__icontains=query)
        all_posts = Post.objects.filter(title__icontains=query)
        all_posts = all_posts.filter(status=1)
        all_projects = Project.objects.filter(title__icontains=query)
        all_services = FSProject.objects.filter(title__icontains=query)
        all_hall_of_fame = HOF.objects.filter(name__icontains=query)
        all_members = TeamMember.objects.filter(name__icontains=query)

    if all_testimonials.count() == 0:
        messages.warning(request, "No se encontraron testimonios en esta\
        búsqueda.")

    if all_posts.count() == 0:
        messages.warning(request, "No se encontró ningún post de blog en esta\
        búsqueda.")

    if all_projects.count() == 0:
        messages.warning(request, "No se encontró ningún proyecto en esta\
        búsqueda.")

    if all_services.count() == 0:
        messages.warning(request, "No se encontraron proyectos de software\
        libre en esta búsqueda.")

    if all_hall_of_fame.count() == 0:
        messages.warning(request, "No se encontraron proyectos del salón de la\
        fama en esta búsqueda.")

    if all_members.count() == 0:
        messages.warning(request, "No se encontraron miembros ó colaboradores\
        en esta búsqueda.")

    context = {
        'all_testimonials' : all_testimonials,
        'all_posts' : all_posts,
        'all_projects' : all_projects,
        'all_services' : all_services,
        'all_hall_of_fame' : all_hall_of_fame,
        'all_members' : all_members,
        'query': query
    }

    return render(request, 'core/results.html', context)
