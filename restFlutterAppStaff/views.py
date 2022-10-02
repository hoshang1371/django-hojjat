from django.shortcuts import render
from django.http.response import HttpResponse ,JsonResponse
from spad_account.models import User
from spad_eshop_products.models import Product
from rest_framework.generics import ListAPIView ,ListCreateAPIView, RetrieveAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializer import ProductSerializer , UserSerializer, MyAuthTokenSerializer
from .permissions import IsSuperUser
#from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response


#! product
class ProductList(ListAPIView):
    queryset  = Product.objects.all()
    serializer_class = ProductSerializer
    #authentication_classes = (SessionAuthentication, )

class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset  = Product.objects.all()
    serializer_class = ProductSerializer
#! user
class UsertList(ListAPIView):
    # queryset  = User.objects.all()
    def get_queryset(self):
        print("_____________________")
        print(self.request.user)
        print(self.request.auth)
        print("_____________________")
        return User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)

class UserDetail(RetrieveAPIView):
    queryset  = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)


# class RevokeToken(APIView):
#     permission_classes =(IsAuthenticated,)

#     def delete(self, request):
#         request.auth.delete()
#         return Response(status=204)


class EmailToken(APIView):
    permission_classes =(IsAuthenticated,)

    def delete(self, request):
        request.auth.delete()
        return Response(status=204)


from rest_framework.authtoken import views as auth_views
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema

class MyAuthToken(auth_views.ObtainAuthToken):
    serializer_class = MyAuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Email",
                        description="Valid email for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )


obtain_auth_token = MyAuthToken.as_view()

#!test
def apage(request):
    return JsonResponse({
                        "Username":"hojjat",
                        "email":"test@test.com",
                        })
