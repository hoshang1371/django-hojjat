from django.contrib import admin

from post_information.models import PostPrice

class PostPriceAdmin(admin.ModelAdmin):
    list_display = ['__str__','title', 'price']

admin.site.register(PostPrice,PostPriceAdmin)

# from .models import PostPrice

# admin.site.register(PostPrice)