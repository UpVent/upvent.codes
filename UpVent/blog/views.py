from django.shortcuts import render

from .models import Post

def Blog(request):
    posts = Post.objects.all()[::-1]
    return render(request, 'blog/blog.html', {'posts':posts})

def BlogEntry(request, article_id):
    post = Post.objects.get(id=article_id)
    return render(request, 'blog/article.html', {'post':post})
