from django.shortcuts import render

from .models import Post

def Blog(request):
    posts = Post.objects.all()[::-1]
    return render(request, 'blog/blog.html', {'posts':posts})

def BlogEntry(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/article.html', {'post':post})
