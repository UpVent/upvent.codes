from django.shortcuts import render
from .models import Resource

def Library(request):
    """
    Display a single detailed view of multiple
    :model:`education.Resource` when clicked
    in the :template:`blog/blog.html` view.
    """

    books = Resource.objects.filter(category='Libro')
    videos = Resource.objects.filter(category='Video')
    other = Resource.objects.filter(category='Otro')

    context = {
        'books': books,
        'videos': videos,
        'other': other
    }

    return render(request, 'education/library.html', context)

def ResView(request, slug):

    """
    Display a single detailed view of a single :model:`education.Resource`
    when clicked in the :template:`education/resource.html` view.
    """

    resource = Resource.objects.get(slug=slug)

    context = {
        'resource': resource
    }

    return render(request, 'education/resource.html', context)
