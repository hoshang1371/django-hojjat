from django.shortcuts import render
from django.views.generic import ListView
from spad_eshop_order.models import Order, OrderDetail
from spad_eshop_products.models import Product

from spad_eshop_products_category.models import ProductCategory 
from django.http import Http404, request
from django.contrib.auth.decorators import login_required


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
    print(order_partials_buy)
    #order_partials = OrderDetail.objects.all()
    Total_price_for_all_product_buy =0

    for order_partial in order_partials_buy:
        Total_price_for_each_product_buy = order_partial.count * order_partial.price
        Total_price_for_all_product_buy = Total_price_for_all_product_buy + Total_price_for_each_product_buy

    contex = {
        'order_partials_buy': order_partials_buy,
        'Total_price_for_all_product_buy' : Total_price_for_all_product_buy,
    }
    return render(request ,'list_of_buy.html',contex)
    
    # return render(request,'list_of_buy.html',)