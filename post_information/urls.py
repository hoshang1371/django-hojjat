from django.urls import path

from post_information.views import add_userPostAddressDetail, edit_post_add_address, post_add_address, post_order, send_code_for_varify_mobile_address


urlpatterns = [
    path('سفارش', post_order ,name="post_order"),
    path('post_add_address', post_add_address ,name="post_add_address"),
    path('edit_post_add_address/<int:pk>', edit_post_add_address ,name="edit_post_add_address"),
    path('add_userPostAddressDetail', add_userPostAddressDetail ,name="add_userPostAddressDetail"),
    path('send_code_for_varify_mobile_address', send_code_for_varify_mobile_address.as_view() ,name="sendCodeForVarifyMobileAddress"),
]