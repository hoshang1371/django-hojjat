from django.contrib import admin

from spad_eshop_order.models import Order,OrderDetail
from django_jalali.admin.filters import JDateFieldListFilter

# you need import this for adding jalali calander widget
import django_jalali.admin as jadmin

class OrderAdmin(admin.ModelAdmin):
    list_filter = (
        ('j_payment_date', JDateFieldListFilter),
    )

admin.site.register(Order, OrderAdmin)

# admin.site.register(Order)
admin.site.register(OrderDetail)