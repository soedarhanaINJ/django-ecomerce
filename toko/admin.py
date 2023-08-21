from django.contrib import admin
from .models import Category, Product

class AdminCategory(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, AdminCategory)

class PostAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'deskripsi')

admin.site.register(Product, PostAdmin)
