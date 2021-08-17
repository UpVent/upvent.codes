from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse

from .models import Post

def Blog(request):

    """
    Display all :model:`blog.Post` saved in the database ordered by ID and
    only those who are marked with status 1 (Published).

    Any blog post marked with status 0 (Draft) will be hidden.

    **Context**

    ``Post``
        An instance of :model:`blog.Post`.

    **Template**
        :template:`blog/blog.html`

    """

    articles = Post.objects.filter(status=1).order_by("created_on")
    paginator = Paginator(articles, 6)

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'blog/blog.html', {'posts':posts})

def BlogEntry(request, slug):

    """
    Display a single detailed view of a single :model:`blog.Post` when clicked
    in the :template:`blog/blog.html` view.

    **Context**

    ``Post``
        - An instance of :model:`blog.Post`
        - The blog post slug for friendly url handling

    **Template**
        :template:`blog/article.html`
    """

    post = Post.objects.get(slug=slug)

    context = {
        'post': post,
    }

    return render(request, 'blog/article.html', context)

def BlogSearch(request):
    results = {'data': []}
    posts = Post.objects.filter(title__icontains=request.POST.get('query'))[:5]
    for post in posts:
        results['data'].append({
            'image': post.image.url,
            'title': post.title,
            'description': post.description[:15],
            'url': post.get_absolute_url(),
        })
    return JsonResponse(results)