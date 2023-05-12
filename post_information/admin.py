from django.contrib import admin

from post_information.models import PostAddressDetail, PostPrice,PostAddress

class PostPriceAdmin(admin.ModelAdmin):
    list_display = ['__str__','title', 'price']

admin.site.register(PostPrice,PostPriceAdmin)
admin.site.register(PostAddress)
admin.site.register(PostAddressDetail)

# from .models import PostPrice

# admin.site.register(PostPrice)