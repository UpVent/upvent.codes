from django.shortcuts import render
from .models import Resource

def Library(request):

    books = Resource.objects.filter(category='Libro')
    videos = Resource.objects.filter(category='Video')
    other = Resource.objects.filter(category='Otro')

    context = {
        'books': books,
        'videos': videos,
        'other': other
    }

    return render(request, 'education/library.html', context)
