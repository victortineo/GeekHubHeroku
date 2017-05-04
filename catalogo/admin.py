from django.contrib import admin

from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'created', 'modified'] # campos que serão exibidos
	search_fields = ['name', 'slug'] # campos de pesquisa
	list_filter = ['created', 'modified']

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'category', 'created', 'modified']
	search_fields = ['name', 'slug', 'category__name'] #category__name busca o nome da categoria
	list_filter = ['created', 'modified', 'category__name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
