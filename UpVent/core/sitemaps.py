from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from blog.models import Post

class StaticViewSitemap(Sitemap):

    changefreq = 'daily'
    priority = 0.5
    protocol = 'https'

    def items(self):
        return [
            'about',
            'blog:home',
            'services',
            'contact:home',
            'licenses',
            'team',
            'privacy-policy',
        ]

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):

    changefreq = 'daily'
    priority = 0.5
    protocol = 'https'

    def items(self):
        Posts = Post.objects.all()
        Posts = Post.objects.filter(status=1)
        return Posts

    def location(self, item):
        return '/' + str(item.slug) + '/'

    def lastmod(self, obj):
        return obj.updated_on
