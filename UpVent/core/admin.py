from django.contrib import admin

# Register your models here.
from .models import Project, FSProject, PrivacyPolicy

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'site', 'created_on')
    list_filter = ('title',)
    search_fields = ['title', 'site']

class FSProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    list_filter = ('title',)
    search_fields = ['title', 'description', 'site', 'created_on']

class PolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')

admin.site.register(Project, ProjectAdmin)
admin.site.register(FSProject, FSProjectAdmin)
admin.site.register(PrivacyPolicy, PolicyAdmin)
