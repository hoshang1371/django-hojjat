from django.contrib import admin

from spad_eshop_order.models import Order,OrderDetail

admin.site.register(Order)
admin.site.register(OrderDetail)