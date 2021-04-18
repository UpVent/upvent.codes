from django.contrib import admin

# Register your models here.
from .models import Project, FSProject, PrivacyPolicy

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'site', 'created_on')
    list_filter = ('title',)
    search_fields = ['title', 'site']

class FSProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'plicense', 'github_addr', 'created_on', 'updated_on')
    list_filter = ('title', 'plicense')
    search_fields = ['title', 'description', 'github_addr', 'created_on']

class PolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')

admin.site.register(Project, ProjectAdmin)
admin.site.register(FSProject, FSProjectAdmin)
admin.site.register(PrivacyPolicy, PolicyAdmin)
