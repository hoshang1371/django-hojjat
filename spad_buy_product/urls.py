from django.urls import path, include

from spad_buy_product.views import List_user_open_order

app_name = "buy"


urlpatterns = [
    # path('list_for_buy', ListOfOrder.as_view() ,name="buyList"),
    path('list_for_buy', List_user_open_order ,name="buyList"),

]
