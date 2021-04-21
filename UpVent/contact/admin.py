from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'email')
    search_fields = ['first_name', 'last_name', 'email']

admin.site.register(Contact, ContactAdmin)
