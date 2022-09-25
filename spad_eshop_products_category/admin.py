from django.contrib import admin

from .models import ProductCategory,ProductCategoryCat


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name']

    class Meta:
        model = ProductCategory


class ProductCategoryAdminOrj(admin.ModelAdmin):
    list_display = ['__str__']

    class Meta:
        model = ProductCategoryCat

admin.site.register(ProductCategory, ProductCategoryAdmin)

admin.site.register(ProductCategoryCat, ProductCategoryAdminOrj)