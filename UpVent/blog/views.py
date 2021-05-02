from django.shortcuts import render

from .models import Post
from .forms import CommentForm

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

    posts = Post.objects.filter(status=1)[::-1]
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
    form = CommentForm

    context = {
        'post': post,
        'form': form
    }

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/article.html', context)

    return render(request, 'blog/article.html', context)
