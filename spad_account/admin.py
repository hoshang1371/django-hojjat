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

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'آخرین کد تایید پیامکی',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'codeVarifySms',
                    'codeVarifySmsDate',
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)


admin.site.register(UserData,UserDataAdmin)

# admin.site.register(User, UserAdmin)
