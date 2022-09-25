from django.contrib import admin
from spad_eshop_tag.models import Tag


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'slug', 'timestamp', 'active']

    class Meta:
        model = Tag

admin.site.register(Tag, ProductAdmin)

#admin.site.register(Tag)