"""UpVent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Import settings if not imported
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

# Import robots.txt
from core.views import robots_txt

# Import sitemaps
from core.sitemaps import StaticViewSitemap, BlogSitemap

handler404 = 'core.views.page_not_found'

sitemaps = {
    'static': StaticViewSitemap,
    'posts': BlogSitemap,
}

urlpatterns = [
    # Special URL's (Mostly admin or managed things)
    path('wp-admin/doc/', include('django.contrib.admindocs.urls')),
    path('captcha/', include('captcha.urls')),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('wp-admin/', admin.site.urls),
    path('robots.txt', robots_txt),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    # Main Site URLs
    path('', include('core.urls'), name='index'),
    path('blog/', include('blog.urls', namespace="blog"), name='blog'),
    path('contact/', include('contact.urls', namespace="contact"),
         name='contact'),
    path('marketcloud/', include('marketcloud.urls', namespace="marketcloud"),
         name='marketcloud'),
    path('education/', include('education.urls', namespace="education"),
         name='education'),
]

admin.site.site_header = "UpVent Admin"
admin.site.index_title = "Admin"
admin.site.site_title = "UpVent"

# Special URL's for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
