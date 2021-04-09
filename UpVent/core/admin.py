from django.contrib import admin

# Register your models here.
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'site', 'created_on')
    list_filter = ('title',)
    search_fields = ['title', 'site']

admin.site.register(Project, ProjectAdmin)
