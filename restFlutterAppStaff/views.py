from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.schemas import ManualSchema
from rest_framework.compat import coreapi, coreschema
from rest_framework.authtoken import views as auth_views
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from spad_account.models import User
from spad_eshop_order.models import Order, OrderDetail
from spad_eshop_products.models import Product
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializer import OrderProductSerializer, ProductSerializer, SearchProductSerializer, UserSerializer, MyAuthTokenSerializer
from .permissions import IsSuperUser
# from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import filters

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
#     permission_classes = (IsSuperUser,)


# class UserDetail(RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperUser,)


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
            return Response(request.data)
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


#! product order staff
import json
from django.http import JsonResponse


class product_order_staff(ListCreateAPIView):
    # queryset = Order.objects.all()
    #queryset = Order.objects.filter(owner_id= request.user.id, is_paid=False).first()
    #queryset = OrderDetail.objects.all()
    serializer_class = OrderProductSerializer
    permission_classes =(IsAdminUser,)
    # filter_fields = ('owner_id', 'is_paid')

    def get(self, request, *args, **kwargs):
        order = Order.objects.filter(owner_id=self.request.user.id).all()

        response =[]
        for val in order.values():
            v  = {
            "owner": val['owner_id'],
            "is_paid": val['is_paid'],
            "payment_date": str(val['payment_date']),
            "j_payment_date": str(val['j_payment_date'])
            }
            response.append(v)
        # response = {
        #   "owner": order.values()[0]['owner_id'],
        #   "is_paid": order.values()[0]['is_paid'],
        #   "payment_date": str(order.values()[0]['payment_date']),
        #   "j_payment_date": str(order.values()[0]['j_payment_date'])
        # }
        # print(response)
        # print(json.dumps(response))
        # print(type(response))
        # return Response(json.dumps(response))
        return JsonResponse(response, safe=False)
        # return JsonResponse(json.dumps(response), safe=False)

        # return JsonResponse(response)
        # return Response(response)
        # return Response({"message": "Hello, world!"})

    def post(self, request, *args, **kwargs):
        order = Order.objects.filter(owner_id=self.request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=self.request.user.id, is_paid=False)
        product_id = int(request.data.get('product'))
        count = int(request.data.get('count'))
        if count < 0:
            count =1
        product = Product.objects.get_by_id(product_id=product_id)
        x= order.orderdetail_set.filter(product_id=product.id)
        if x:
            print("exist")
            print(x.values()[0]['count'])
            x.update(count=count+x.values()[0]['count'])
        else:
            print("NO exist")
            order.orderdetail_set.create(product_id=product.id, price=product.price ,count=count)
           #TODO
        return Response(request.data)

    # def get_queryset(self):
    #     #ownerId = self.kwargs['owner']
    #     queryset = Order.objects.all()
    #     print("++++++++++++++++++++")
    #     print(self.request.user)
    #     print(self.request.user.id)

    #     order = Order.objects.filter(
    #         owner_id=self.request.user.id, is_paid=False).first()
    #     if order is None:
    #         order = Order.objects.create(
    #             owner_id=self.request.user.id, is_paid=False)

    #     x = order.orderdetail_set.all()
    #     print(x)
    #     return queryset

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


#!test


def apage(request):
    return JsonResponse({
                        "Username": "hojjat",
                        "email": "test@test.com",
                        })
