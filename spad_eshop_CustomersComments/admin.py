from django.contrib import admin
from spad_eshop_CustomersComments.models import CustomerComment

class CustomerCommentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'subject', 'is_ok']
    list_filter = ['is_ok']
    list_editable = ['is_ok']
    search_fields = ['subject']

admin.site.register(CustomerComment,CustomerCommentAdmin)
