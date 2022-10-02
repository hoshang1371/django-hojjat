from django.urls import path, include
from .views import apage, ProductList, ProductDetail, UsertList, UserDetail \
                ,obtain_auth_token
                #  ,  RevokeToken
# from rest_framework.authtoken.views import obtain_auth_token

app_name = "api"

urlpatterns = [
    path('core', apage),
    path("",ProductList.as_view(), name="list"),
    path("<int:pk>",ProductDetail.as_view(), name="detail"),
    path("user/",UsertList.as_view(), name="user-list"),
    path("user/<int:pk>",UserDetail.as_view(), name="user-detail"),
    # #! Token authentication
    # path('token_auth/', obtain_auth_token),
    # #! Revoke Token
    # path('revoke',RevokeToken.as_view()),
    #!login with email
    path('api_token_auth/', obtain_auth_token),
    #!dj_rest_auth
    # path('rest_auth/', include('dj_rest_auth.urls')),
    # path('dj_rest_auth/registration/', include('dj_rest_auth.registration.urls'))


]