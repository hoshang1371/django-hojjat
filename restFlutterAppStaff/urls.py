from django.urls import path, include
from .views import apage, ProductList, ProductDetail,UsertList,USERDetail

app_name = "api"

urlpatterns = [
    path('core', apage),
    path("",ProductList.as_view(), name="list"),
    path("<int:pk>",ProductDetail.as_view(), name="detail"),
    path("user/",UsertList.as_view(), name="user-list"),
    path("user/<int:pk>",USERDetail.as_view(), name="user-detail"),
]