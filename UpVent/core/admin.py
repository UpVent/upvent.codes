from django.contrib import admin

# Register your models here.
from .models import (Testimonial,
                     Project,
                     FSProject,
                     License,
                     HOF,
                     TeamMember,
                     PrivacyPolicy,
                     TOS)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'workplace', 'site')
    list_filter = ('name', 'workplace')
    search_fields = ['name', 'workplace', 'site']
    empty_value_display = '-vacío-'

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'site', 'created_on')
    list_filter = ('title',)
    search_fields = ['title', 'site']
    empty_value_display = '-vacío-'

class FSProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'plicense', 'github_addr', 'created_on',
                    'updated_on')
    list_filter = ('title', 'plicense')
    search_fields = ['title', 'description', 'github_addr', 'created_on']
    empty_value_display = '-vacío-'

class LicenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'license_link')
    list_filter = ('name',)
    search_fields = ['name', 'license_link']
    empty_value_display = '-vacío-'

class HOFAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name', ]
    empty_value_display = '-vacío-'

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    list_filter = ('name', 'position')
    search_fields = ['name', 'position']
    empty_value_display = '-vacío-'

class PolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    empty_value_display = '-vacío-'

class TOSAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    empty_value_display = '-vacío-'

admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(FSProject, FSProjectAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(HOF, HOFAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(PrivacyPolicy, PolicyAdmin)
admin.site.register(TOS, TOSAdmin)
