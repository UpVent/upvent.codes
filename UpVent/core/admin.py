from django.contrib import admin

# Register your models here.
from .models import Project, FSProject, License, HOF, TeamMember, PrivacyPolicy

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'site', 'created_on')
    list_filter = ('title',)
    search_fields = ['title', 'site']

class FSProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'plicense', 'github_addr', 'created_on', 'updated_on')
    list_filter = ('title', 'plicense')
    search_fields = ['title', 'description', 'github_addr', 'created_on']

class LicenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'license_link')
    list_filter = ('name',)
    search_fields = ['name', 'license_link']

class HOFAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name', ]

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    list_filter = ('name', 'position')
    search_fields = ['name', 'position']

class PolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')

admin.site.register(Project, ProjectAdmin)
admin.site.register(FSProject, FSProjectAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(HOF, HOFAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(PrivacyPolicy, PolicyAdmin)
