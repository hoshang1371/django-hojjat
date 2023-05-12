from cgi import print_environ
from django.shortcuts import render, redirect
from spad_eshop_slider.models import Slider
from spad_eshop_order.models import OrderDetail,Order
from spad_eshop_products.models import Product
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from spad_eshop_settings.models import SiteSetting
from spad_eshop_products_category.models import ProductCategory, ProductCategoryCat


def home_page(request):
    sliders = Slider.objects.all()
    site_setting = SiteSetting.objects.first()
    most_visit_product = Product.objects.order_by('-visit_count').all()[:15]
    latest_products = Product.objects.order_by('-id').all()[:10]
    # print(latest_products)
    vige_products = Product.objects.order_by('-vige').all()[:10]
    
    username = request.user.username
    # print(username)

    context = {
        'data': 'new data',
        'sliders' : sliders,
        'setting': site_setting,
        'most_visit' : most_visit_product,
        'latest_products' : latest_products,
        'vige_products' : vige_products,
        'username' : username,
    }
    return render(request, 'home_page.html', context)

def about_page(request):
    site_setting = SiteSetting.objects.first()
    username = request.user.username
    contex = {
        'setting': site_setting,
        'username' : username,
    }
    return render(request, 'about_page.html',contex)

def about_page_footer(request):
    site_setting = SiteSetting.objects.first()
    # username = request.user.username
    contex = {
        'setting': site_setting,
        # 'username' : username,
    }
    return render(request, 'shared/about_page_footer.html',contex)

def about_page_header(request):
    site_setting = SiteSetting.objects.first()
    contex = {
        'setting': site_setting
    }
    return render(request, 'shared/_HeaderRefrences.html',contex)

def products_number_all_order_partial(request):
    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()

    if order is None:
        order = Order.objects.create(owner_id=request.user.id, is_paid=False)   
         
    order_count_partials = order.orderdetail_set.all()
    #order_count_partials = OrderDetail.objects.all()
    Total_count_for_all_product =0
    for order_count_partial in order_count_partials:
        Total_count_for_all_product = Total_count_for_all_product + order_count_partial.count

    contex = {
        'Total_count_for_all_product' : Total_count_for_all_product
    }
    return render(request ,'shared/products_number_all_order_partial.html',contex)

def products_category(request):
    categories = ProductCategoryCat.objects.all()
    
    Cates_0 = ProductCategory.objects.filter(catCategory= categories[0]).all()
    Cates_1 = ProductCategory.objects.filter(catCategory= categories[1]).all()
    Cates_2 = ProductCategory.objects.filter(catCategory= categories[2]).all()
    contex = {
        'categories': categories,
        'Cates_0': Cates_0,
        'Cates_1': Cates_1,
        'Cates_2': Cates_2,
    }
    return render(request ,'shared/products_category.html',contex)

def products_order_partial(request):
    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()

    if order is None:
        order = Order.objects.create(owner_id=request.user.id, is_paid=False)

    order_partials = order.orderdetail_set.all()
    # print("order_partials=",order_partials)
    #order_partials = OrderDetail.objects.all() orderdetail_set
    Total_price_for_all_product =0

    for order_partial in order_partials:
        Total_price_for_each_product = order_partial.count * order_partial.price
        Total_price_for_all_product = Total_price_for_all_product + Total_price_for_each_product

    contex = {
        'order_partials': order_partials,
        'Total_price_for_all_product' : Total_price_for_all_product,
    }
    return render(request ,'shared/product_order_partial.html',contex)

#@login_required(login_url='/login')

class CreateOneOrder(View):
    def  get(self, request):
        Total__each_product =0

        product_id = request.GET.get('id', None)

        order = Order.objects.filter(owner_id= request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=self.request.user.id, is_paid=False)
        
        # product = Product.objects.get_by_id(
        #     product_id=product_id
        #     )

        product = Product.objects.get_by_id(product_id=product_id)
        order_partial= order.orderdetail_set.filter(product_id=product.id)
        # print("olk")
        # print(order_partial)
        # print("product.number= ",product.number)

        if( 1 > int(product.number)):
            data = {
                'eerorNumberOfStore': True
            }
            
            return JsonResponse(data)

        # order_partial = OrderDetail.objects.filter(product_id=product.id).first()
        #order_partial = order.orderdetail_set.filter(product_id=product.id).first()
        #if order_partial[0] is None:
        if not order_partial:
            
            order.orderdetail_set.create(
                product_id=product.id, 
                price=product.price ,
                count=1
                ) 
            #order_partial = OrderDetail.objects.get(product_id=product.id)
            order_partial_set = order.orderdetail_set.get(product_id=product.id)
            print(order_partial_set)
            Total__each_product = int(order_partial_set.count) * int(order_partial_set.price)

            order_count_partials = order.orderdetail_set.all()
            print(order_count_partials)
            Total_count_for_all_product =0
            Total_count_for_product =0
            for order_count_partial in order_count_partials:
                Total_count_for_all_product = Total_count_for_all_product + order_count_partial.count
                Total_count_for_product =Total_count_for_product+1

            #print(Total_count_for_product)
            user = {'productId':order_partial_set.id,
                    'productImage':order_partial_set.product.image.url,
                    'productName':order_partial_set.product.title,
                    'productCount':order_partial_set.count,
                    'product_All_price':Total__each_product,
                    'Total_count_for_all_product':Total_count_for_all_product,
                    'Total_count_for_product' : Total_count_for_product,
                }
            data = {
                'user': user,
                'addedOne': True
            }
            return JsonResponse(data)

        data = {
            'addedOne': False
        }
        
        return JsonResponse(data)

class UpdateCrudUser(View):
    def  get(self, request):

        id1 = request.GET.get('id', None)
        count1 = request.GET.get('count', None)
        #order_partials = OrderDetail.objects.all()

        order = Order.objects.filter(owner_id= request.user.id, is_paid=False).first()

        obj = order.orderdetail_set.get(id=id1)
        # obj = OrderDetail.objects.get(id=id1)
        obj.count = count1
        
        
        obj.save()

        Total__each_product = int(obj.count) * int(obj.price)

        #order_count_partials = OrderDetail.objects.all()
        order_count_partials = order.orderdetail_set.all()
        Total_count_for_all_product =0
        for order_count_partial in order_count_partials:
            Total_count_for_all_product = Total_count_for_all_product + order_count_partial.count
       
        
        user = {
            'id':obj.id,
            'count':obj.count,
            'price':Total__each_product,
            'Total_count_for_all_product' : Total_count_for_all_product
            }

        data = {
            'user': user
        }
        return JsonResponse(data)

#@login_required(login_url='/login')
class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        OrderDetail.objects.get(id=id1).delete()
        order = Order.objects.filter(owner_id= request.user.id, is_paid=False).first()
        # order_count_partials = OrderDetail.objects.all()
        order_count_partials = order.orderdetail_set.all()

        Total_count_for_all_product =0
        Total_price_for_all_product =0
        Total_count_for_product =0

        for order_count_partial in order_count_partials:
            Total_count_for_all_product = Total_count_for_all_product + order_count_partial.count       
            Total_price_for_all_product = Total_price_for_all_product + (int(order_count_partial.price)*order_count_partial.count)
            Total_count_for_product =Total_count_for_product+1        
        #print(Total_price_for_all_product)
        user = {
            'Total_count_for_all_product':Total_count_for_all_product,
            'Total_price_for_all_product' : Total_price_for_all_product,
            'Total_count_for_product': Total_count_for_product,
            }
        # delete = {
        #     'deleted': True,
        # }
        data = {
            #'deleted': True,
            'user': user,
        }
        return JsonResponse(data)

class DeleteCrudUserAll(View):
    def  get(self, request):
        OrderDetail.objects.all().delete()
        #print("ok")
        data = {
            'deleted': True
        }
        return JsonResponse(data)