from django.shortcuts import render
# from django.views.generic import ListView
from spad_buy_product.serializer import OrderProductDeleteListOfBuySerializer, OrderProductSerializerForListOfbuy
from spad_eshop_order.models import Order, OrderDetail
# from spad_eshop_products.models import Product

# from spad_eshop_products_category.models import ProductCategory 
from django.http import Http404, request
from django.contrib.auth.decorators import login_required

from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView,
    DestroyAPIView, UpdateAPIView)
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from spad_eshop_products.models import Product
from rest_framework.authentication import SessionAuthentication

from rest_framework.response import Response
from django.http.response import HttpResponse, JsonResponse
from post_information.models import PostPrice
from spad_eshop_settings.models import SiteSetting
# class ListOfOrder(ListView):
#     template_name = '/list_of_buy.html'
#     model = OrderDetail

    # paginate_by = 4

    # def get_queryset(self):
    #     pass
        # category_name = self.kwargs['category_name']
        # category = ProductCategory.objects.filter(name__iexact=category_name).first()
        # if category is None:
        #     raise Http404('صفحه ی مورد نظر یافت نشد')
        # return Product.objects.get_products_by_category(category_name)


@login_required(login_url='/login')
def List_user_open_order(request):
    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    order_partials_buy = order.orderdetail_set.all()
    post_price = PostPrice.objects.filter().first()
    print("post_price=",post_price.price)
    # print(order_partials_buy)
    #order_partials = OrderDetail.objects.all()
    Total_price_for_all_product_buy =0
    count_off_all_product =0

    for order_partial in order_partials_buy:
        count_off_all_product = count_off_all_product+1
        Total_price_for_each_product_buy = order_partial.count * order_partial.price
        Total_price_for_all_product_buy = Total_price_for_all_product_buy + Total_price_for_each_product_buy
    username = request.user.username
    site_setting = SiteSetting.objects.first()

    contex = {
        'username' : username,
        'setting': site_setting,
        'order_partials_buy': order_partials_buy,
        'Total_price_for_all_product_buy' : Total_price_for_all_product_buy,
        'post_price': post_price.price,
        'count_off_all_product': count_off_all_product,
    }
    return render(request ,'list_of_buy.html',contex)
    
    # return render(request,'list_of_buy.html',)
#! buy/update_for_buy


class product_order_List_buy(UpdateAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderProductSerializerForListOfbuy
    permission_classes = [IsAuthenticated]
    authentication_classes = (SessionAuthentication, )
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        order = Order.objects.filter(
            owner_id=self.request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(
                owner_id=self.request.user.id, is_paid=False)
        product_id = int(request.data.get('id'))
        count = int(request.data.get('count'))

        post_price = PostPrice.objects.filter().first()

        if count < 0:
            count = 1
        # product = Product.objects.get_by_id(product_id=product_id)
        x = order.orderdetail_set.filter(id=product_id)
        if x:
            x.update(count=count)


        order_partials_buy = order.orderdetail_set.all()
        print("order_partial_buy.count 1 order_partial_buy.price",int(x.values()[0]['count'])*int(x.values()[0]['price']))
        Total_price_for_all_product_buy =0
        count_off_all_product =0
        count_all=0
        for order_partial in order_partials_buy:
            count_off_all_product =count_off_all_product+1
            count_all =count_all +order_partial.count
            Total_price_for_each_product_buy = order_partial.count * order_partial.price
            Total_price_for_all_product_buy = Total_price_for_all_product_buy + Total_price_for_each_product_buy
        Total_price_postPrice = Total_price_for_all_product_buy + post_price.price
        # print("Total_price=", Total_price)
        print('count_all=',count_all);

        response = {
            "id": x.values()[0]['id'],
            "count": x.values()[0]['count'],
            "price": x.values()[0]['price'],
            "Total_price_for_all_product_buy" : Total_price_for_all_product_buy,
            "count_off_all_product" : count_off_all_product,
            "Total_price_postPrice" : Total_price_postPrice,
            "count_all" : count_all,
        }


        return JsonResponse(response, safe=False)
        # return Response(request.data)



# class ProductList(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


#! delete product order detail
class Order_product_delete_list_of_buy(DestroyAPIView):
    queryset = OrderDetail.objects.all()
    #queryset = Order.objects.filter(owner_id= request.user.id, is_paid=False).first()
    #queryset = OrderDetail.objects.all()
    serializer_class = OrderProductDeleteListOfBuySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (SessionAuthentication, )
