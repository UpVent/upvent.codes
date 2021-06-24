from django.shortcuts import render

def Library(request):

    return render(request, 'education/library.html', {})
