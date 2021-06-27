from django.contrib import admin

from .models import Resource

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category')
    list_filter = ("category",)
    search_fields = ['title', 'category']
    prepopulated_fields = { 'slug': ('title',) }

admin.site.register(Resource, ResourceAdmin)
