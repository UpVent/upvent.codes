from django.shortcuts import render


# Create your views here.
def index(request):
    index = ['01']
    return render(request, 'core/index.html', {'index': index})
