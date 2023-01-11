import json
from django.core import serializers
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework import status
from django.core.files.base import ContentFile
import base64
from django.db.models import Q
from datetime import datetime, timedelta
import os
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.schemas import ManualSchema
from rest_framework.compat import coreapi, coreschema
from rest_framework.authtoken import views as auth_views
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from extentions.images import to_internal_value
from spad_account.models import User
from spad_eshop_order.models import Order, OrderDetail
from spad_eshop_products.models import Product
from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView,
    DestroyAPIView, UpdateAPIView)
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from spad_eshop_products_category.models import ProductCategory, ProductCategoryCat
from .serializer import AddProductSerializer, OrderDeleteSerializer, OrderProductDeleteSerializer, OrderProductSerializer, OrderProductUpdateSerializer, ProductSerializer, SearchProductSerializer, UserSerializer, MyAuthTokenSerializer
from .permissions import IsStaffOrReadOnly, IsSuperUser
# from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import filters
from django.http import JsonResponse

#! product

# @api_view(['GET'])


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = (SessionAuthentication, )

# @api_view(['GET'])


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
#! user


# class UsertList(ListAPIView):
#     def get_queryset(self):
#         return User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsStaffOrReadOnly,)


# class UserDetail(RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsStaffOrReadOnly,)


# class RevokeToken(APIView):
#     permission_classes =(IsAuthenticated,)

#     def delete(self, request):
#         request.auth.delete()
#         return Response(status=204)


class EmailToken(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        request.auth.delete()
        return Response(status=204)


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


#!check Token


@api_view(['GET', 'POST'])
def CheckToken(request):
    if request.method == 'POST':
        # print(type(request.data))
        # print(request.data["token"])
        if Token.objects.filter(pk=request.data["token"]).exists():
            user = Token.objects.get(pk=request.data["token"]).user
            print(user.id)
            # return Response(request.data)
            return Response(
                {
                    'token': request.data["token"],
                    # 'token': token.key,
                    'username': user.username,
                    'userid': user.id
                })
        else:
            return Response({"token": "token is distroy"})
    return Response({"message": "Hello, world!"})

#! search
# http://192.168.1.51:8000/api/questions/?search=
# @api_view(['GET'])


class SearchProductAPIView(generics.ListCreateAPIView):
    #search_fields = ['title','description','smallDescription']
    search_fields = ['title', 'code', 'place']
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = SearchProductSerializer


class SearchProductWithOnlyPlaceAPIView(generics.ListCreateAPIView):
    #search_fields = ['title','description','smallDescription']
    search_fields = ['place']
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = SearchProductSerializer

class AddProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = AddProductSerializer
    permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        img = to_internal_value(self, request)

        product = Product(
            title=request.data.get('title'),
            code=request.data.get('code'),
            place=request.data.get('place'),
            number=request.data.get('number'),
            brand=request.data.get('brand'),
            description=request.data.get('description'),
            smallDescription=request.data.get('smallDescription'),
            price=request.data.get('price'),
            priceOff=request.data.get('priceOff'),
            active=request.data.get('active'),
            vige=request.data.get('vige'),
            image=img
        )

        # product.image = img

        product.save()
        # serialized_obj = serializers.serialize('json', [ product, ])
        serialized_obj = serializers.serialize('json', [product, ])
        struct = json.loads(serialized_obj)
        # serialized_obj = json.dumps(struct[0])
        cat = ProductCategory.objects.all()
        data = list(cat.values())

        newdata = {}
        for entry in data:
            # remove and return the name field to use as a key
            name = entry.pop('name')
            newdata[name] = entry
        # qs_json = serializers.serialize('json', cat)
        # print(type(data))
        # struct_cat = json.loads(serialized_cat)
        # todo
        serialized_obj = json.dumps(
            {"product": struct[0], "category": newdata}, ensure_ascii=False)
        # serialized_obj = json.dumps(struct[0])
        # print(cat)
        return Response({"message": "product is added"})
        # return super().post(request, *args, **kwargs)


#! product order staff
# Sample.objects.filter(date__range=[startdate, enddate]) payment_date


class product_order_staff(ListCreateAPIView):
    serializer_class = OrderProductSerializer
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        startdate = datetime.today()
        enddate = startdate - timedelta(days=6)
        print(startdate)
        print(enddate)
        # order = Order.objects.filter(owner_id=self.request.user.id)
        # order1 = Order.objects.filter(payment_date__range=["2022-10-23", "2022-10-29"])
        # print(order1)
        order = Order.objects.filter(Q(owner_id=self.request.user.id) & Q(
            payment_date__range=[enddate, startdate])).all()
        response = []
        for val in order.values():
            v = {
                "id": val['id'],
                "owner": val['owner_id'],
                "is_paid": val['is_paid'],
                "payment_date": str(val['payment_date']),
                "j_payment_date": str(val['j_payment_date'])
            }
            response.append(v)
        return JsonResponse(response, safe=False)
        # return JsonResponse(json.dumps(response), safe=False)

        # return JsonResponse(response)
        # return Response(response)
        # return Response({"message": "Hello, world!"})

    def post(self, request, *args, **kwargs):
        order = Order.objects.filter(
            owner_id=self.request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(
                owner_id=self.request.user.id, is_paid=False)
        product_id = int(request.data.get('product'))
        count = int(request.data.get('count'))
        if count < 0:
            count = 1
        product = Product.objects.get_by_id(product_id=product_id)
        x = order.orderdetail_set.filter(product_id=product.id)
        if x:
            print("exist")
            print(x.values()[0]['count'])
            # x.update(count=count+x.values()[0]['count'])
            x.update(count=count)
        else:
            print("NO exist")
            order.orderdetail_set.create(
                product_id=product.id, price=product.price, count=count)
           # TODO
        return Response(request.data)

#! product list order staff


class product_order_ditails_staff(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        order_id = self.kwargs.get('order_id')
        orderDetails = OrderDetail.objects.filter(order=order_id)
        response = []
        total_price = 0
        for orderDetail in orderDetails:
            product = Product.objects.filter(title=orderDetail.product)
            print(orderDetail.price * orderDetail.count)
            total_price = total_price + (orderDetail.price * orderDetail.count)
            v = {
                "id_order": orderDetail.id,
                "orderDetail_count_price": orderDetail.price * orderDetail.count,
                "id": product[0].id,
                "code": product[0].code,
                "title": product[0].title,
                "place": product[0].place,
                "count": orderDetail.count,
                "brand": product[0].brand,
                "description": product[0].description,
                "smallDescription": product[0].smallDescription,
                "price": product[0].price,
                "priceOff": product[0].priceOff,
                "image": product[0].image.url,
                "image_tumpnail": product[0].image_tumpnail.url,
                "active": str(product[0].active).lower(),
                "visit_count": product[0].visit_count,
                "vige": str(product[0].vige).lower(),

            }
            response.append(v)
        print("total_price", total_price)
        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})
# @api_view(['POST'])
# def product_order_staff(request):

#     print(type(request.data))
#     if request.method == 'POST':
#         print(type(request.data))
        # order = Order.objects.filter(owner_id= request.user.id, is_paid=False).first()
        # if order is None:
        #     order = Order.objects.create(owner_id=request.user.id, is_paid=False)

        # serializer = SnippetSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#! delete product order detail


class product_order_delete_staff(DestroyAPIView):
    queryset = OrderDetail.objects.all()
    #queryset = Order.objects.filter(owner_id= request.user.id, is_paid=False).first()
    #queryset = OrderDetail.objects.all()
    serializer_class = OrderProductDeleteSerializer
    permission_classes = (IsAdminUser,)

#! delete product order detail


class order_delete_staff(DestroyAPIView):
    queryset = Order.objects.all()
    #queryset = Order.objects.filter(owner_id= request.user.id, is_paid=False).first()
    #queryset = OrderDetail.objects.all()
    serializer_class = OrderDeleteSerializer
    permission_classes = (IsAdminUser,)

#! update is paid order


class isPaid_order_update_staff(UpdateAPIView):
    queryset = Order.objects.all()
    #queryset = Order.objects.filter(owner_id= request.user.id, is_paid=False).first()
    serializer_class = OrderProductUpdateSerializer
    lookup_field = 'id'
    permission_classes = (IsAdminUser,)

#!test


def apage(request):
    return JsonResponse({
                        "Username": "hojjat",
                        "email": "test@test.com",
                        })
