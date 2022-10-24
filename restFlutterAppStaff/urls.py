from django.urls import path, include

from .views import SearchProductAPIView, apage,\
                   ProductList, ProductDetail,\
                   obtain_auth_token,CheckToken, product_order_ditails_staff, product_order_staff
                   #UsertList, UserDetail, \
                #  ,  RevokeToken
# from rest_framework.authtoken.views import obtain_auth_token

app_name = "api"

urlpatterns = [
    path('core', apage),
    path("",ProductList.as_view(), name="list"),
    path("<int:pk>",ProductDetail.as_view(), name="detail"),
    # path("user/",UsertList.as_view(), name="user-list"),
    # path("user/<int:pk>",UserDetail.as_view(), name="user-detail"),

    #! Token authentication
    # path('token_auth/', obtain_auth_token),
    # #! Revoke Token
    # path('revoke',RevokeToken.as_view()),
    #!login with email
    path('api_token_auth/', obtain_auth_token),
    #! check Token
    path('Check_token/', CheckToken),
    #!search url
    path('questions/', SearchProductAPIView.as_view()),
    #!product order staff url
    path('product_order_staff/', product_order_staff.as_view()),
    #!product order ditails staff url
    path('product_order_ditails_staff/<order_id>/', product_order_ditails_staff.as_view())

    #!dj_rest_auth
    # path('rest_auth/', include('dj_rest_auth.urls')),
    # path('dj_rest_auth/registration/', include('dj_rest_auth.registration.urls'))


]