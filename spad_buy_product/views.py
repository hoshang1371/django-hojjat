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
    return render(request,'list_of_buy.html',)