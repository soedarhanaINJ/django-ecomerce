from django.contrib import admin
from .models import Product

class PostAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'deskripsi')

admin.site.register(Product, PostAdmin)