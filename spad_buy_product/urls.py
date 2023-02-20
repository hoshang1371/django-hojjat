from django.urls import path, include
# from spad_buy_product.serializer import OrderProductDeleteListOFBuySerializer

from spad_buy_product.views import List_user_open_order, Order_product_delete_list_of_buy,product_order_List_buy

app_name = "buy"


urlpatterns = [
    # path('list_for_buy', ListOfOrder.as_view() ,name="buyList"),
    path('list_for_buy', List_user_open_order ,name="buyList"),
    path('update_for_buy/', product_order_List_buy.as_view() ,name="UpdateForBuyList"),
    #!product order delete staff url
    path('Order_product_delete_list_of_buy/<int:pk>', Order_product_delete_list_of_buy.as_view()),

]
