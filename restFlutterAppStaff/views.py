from django.shortcuts import render
from django.http.response import HttpResponse ,JsonResponse
from spad_account.models import User
from spad_eshop_products.models import Product
from rest_framework.generics import ListAPIView ,ListCreateAPIView, RetrieveAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from .serializer import ProductSerializer , UserSerializer
from .permissions import IsSuperUser
#! product
class ProductList(ListAPIView):
    queryset  = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset  = Product.objects.all()
    serializer_class = ProductSerializer
#! user
class UsertList(ListAPIView):
    queryset  = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)

class USERDetail(RetrieveAPIView):
    queryset  = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)


#!test
def apage(request):
    return JsonResponse({
                        "Username":"hojjat",
                        "email":"test@test.com",
                        })
