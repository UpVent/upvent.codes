from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from blog.models import Post
from marketcloud.models import Product

class StaticViewSitemap(Sitemap):
    """
      Esta clase genera el sitemap para las vistas estáticas de UpVent.
    """

    changefreq = 'daily'
    priority = 0.5
    protocol = 'https'

    def items(self):
        return [
            'about',
            'blog:home',
            'services',
            'contact:home',
            'marketcloud:home',
            'licenses',
            'team',
            'privacy-policy',
            'terms-of-service',
        ]

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):

    """
        Esta clase genera el sitemap de los artículos del blog publicados en
        UpVent
    """

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

class ProductSitemap(Sitemap):

    """
        Esta clase genera el sitemap de los productos de la tienda,
        publicados en UpVent
    """

    changefreq = 'daily'
    priority = 0.5
    protocol = 'https'

    def items(self):
        Products = Product.objects.all()
        Products = Product.objects.filter(status=1)
        return Products

    def location(self, item):
        return '/' + str(item.slug) + '/'

    def lastmod(self, obj):
        return obj.updated_on
