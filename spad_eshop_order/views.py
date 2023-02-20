from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# from django.shortcuts import render_to_response

from spad_eshop_order.forms import UserNewOrderForm
from spad_eshop_order.models import Order, OrderDetail
from spad_eshop_products.models import Product

from django.contrib import messages



@login_required(login_url='/login')
def add_user_order(request):
    # print("hojjat")
    new_order_form = UserNewOrderForm(request.POST or None)

    if new_order_form.is_valid():
       # print("ok")
        order = Order.objects.filter(
            owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(
                owner_id=request.user.id, is_paid=False)
        product_id = new_order_form.cleaned_data.get('product_id')
        count = new_order_form.cleaned_data.get('count')
        if count < 0:
            count = 1
        product = Product.objects.get_by_id(product_id=product_id)
        # TODO if order is exsist
        x = order.orderdetail_set.filter(product_id=product.id)
        #* agar kala dar sabad kharid mojod bood
        if x:
            messages.success(request, 'این کالا در سبد خرید موجوداست.')
            return redirect(f'/products/{product.id}/{product.title.replace(" ","-")}')
        else :
            order.orderdetail_set.create(product_id=product.id, price=product.price ,count=count)
        # todo: redirect user to user panel
        messages.success(request, "محصول مورد نظر به سبد خرید اضافه شد.")       
        return redirect('/products')
        # return redirect(f'/products/{product.id}/{product.title.replace(" ","-")}')

    return redirect('/')

@login_required(login_url='/login')
def user_open_order(request):
    contex ={
        'order': None,
        'details': None
    }
    open_order : Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()

    if open_order is not None:
        contex['order'] = open_order
        contex['details'] = open_order.orderdetail_set.all()

    return render(request,'order/user_open_order.html',contex)

@login_required(login_url='/login')
def remove_order_detail(request, *args, **kwargs):
    detail_id = kwargs.get('detail_id')
    if detail_id is not None:
        order_detail = OrderDetail.objects.get_queryset().get(id=detail_id, order__owner_id=request.user.id)
        if order_detail is not None:
            order_detail.delete()
    return redirect('/open-order')