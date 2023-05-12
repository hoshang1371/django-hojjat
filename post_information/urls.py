from django.urls import path

from post_information.views import add_userPostAddressDetail, post_order


urlpatterns = [
    path('سفارش', post_order ,name="post_order"),
    path('add_userPostAddressDetail', add_userPostAddressDetail ,name="add_userPostAddressDetail"),
]