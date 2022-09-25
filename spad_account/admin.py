from django.contrib import admin


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User



# Register your models here.
from .models import UserData

class UserDataAdmin(admin.ModelAdmin):
    list_display = ['__str__','choiceField', 'SAL', 'MAH', "ROZ"]
    
    class Meta:
        model = UserData

# class UserinfoAdmin(admin.ModelAdmin):
#     list_display = ['__str__','choicefield', 'SAL']
    
#     class Meta:
#         model = UserData

admin.site.register(UserData,UserDataAdmin)

admin.site.register(User, UserAdmin)
