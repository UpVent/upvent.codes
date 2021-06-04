from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'status', 'price', 'category', 'created_on')
    list_filter = ("status",)
    search_fields = ['name', 'price', 'category', 'created_on']
    prepopulated_fields = { 'slug': ('name',) }

admin.site.register(Product, ProductAdmin)
