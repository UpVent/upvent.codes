from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET

from blog.models import Post

from .models import (Testimonial,
                     Project,
                     FSProject,
                     License,
                     HOF,
                     TeamMember,
                     PrivacyPolicy,
                     TOS)

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

    context = {
        'testimonials': testimonials
    }

    return render(request, 'core/index.html', context)

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

    context = {
        'projects': projects
    }

    return render(request, 'core/about.html', context)

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

    context = {
        'services': services
    }

    return render(request, 'core/services.html', context)

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

    members = TeamMember.objects.filter(is_collab=False)
    collabs = TeamMember.objects.filter(is_collab=True)

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

    context = {
        'policies': policies
    }

    return render(request, 'core/privacy-policy.html', context)


def terms_service(request):

    """
    Display the "terms-of-service" page for this site.

    **Context**

    ``policies``
        Return the only instance of the :model:`marketcloud.TOS`
        saved in the database. This model allows ONLY ONE entry policy.

    **Template**
        :template:`marketcloud/tos.html`

    """

    policies = TOS.objects.all().first()

    context = {
        'policies': policies
    }

    return render(request, 'core/tos.html', context)

@require_GET
def robots_txt(request):
    """
        This renders a robots.txt file

        Modify this in production, these URL's are used as an example for
        forkers. Do this especially if you changed your admin site url.
    """
    lines = [
        "Sitemap: https://upvent.codes/sitemap.xml",
        "User-Agent: *",
        "Crawl-delay: 120",
        "Disallow: /admin/",
        "Disallow: /administration/",
        "Disallow: /administrator/",
        "Disallow: /administrador/",
        "Disallow: /administracion/",
        "Disallow: /wp-admin/",
        "Disallow: /category/",
        "Disallow: /tag/"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def page_not_found(request, exception):
    """
        This is a customized 404 error page when the server doesn't find
        any requested page.
    """
    return render(request, 'core/404.html', status=404)
