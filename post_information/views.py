from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from post_information.forms import UserPostAddressDetailForm
from post_information.models import PostAddressDetail, PostPrice,PostAddress

from spad_eshop_order.models import Order


@login_required(login_url='/login')
def post_order(request):
    postAddressesUser = PostAddress.objects.filter(owner_id=request.user.id)
    #! forms of postaddress
    user_post_address_detail = UserPostAddressDetailForm(request.POST or None,request.user)#
    # if request.method == 'POST':
    if user_post_address_detail.is_valid():
        product_id = user_post_address_detail.cleaned_data.get('PostAddress_id')
        # print('product_id=',product_id)
    #!
    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    order_partials_buy = order.orderdetail_set.all()
    post_price = PostPrice.objects.filter().first()
    #order_partials = OrderDetail.objects.all()
    Total_price_for_all_product_buy =0
    count_off_all_product =0

    for order_partial in order_partials_buy:
        count_off_all_product = count_off_all_product+1
        Total_price_for_each_product_buy = order_partial.count * order_partial.price
        Total_price_for_all_product_buy = Total_price_for_all_product_buy + Total_price_for_each_product_buy
    # print('user_post_address_detail=',user_post_address_detail['PostAddress_id'])

    contex = {
        # 'order_partials_buy': order_partials_buy,
        'postAddressesUser' : postAddressesUser,
        'Total_price_for_all_product_buy' : Total_price_for_all_product_buy,
        'post_price': post_price.price,
        'count_off_all_product': count_off_all_product,
        'user_post_address_detail':user_post_address_detail['PostAddress_id'],
        'zipee' : zip(user_post_address_detail['PostAddress_id'],postAddressesUser),
    }
    return render(request ,'post_order.html',contex)


@login_required(login_url='/login')
def add_userPostAddressDetail(request):
    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    postAddressesUser = PostAddress.objects.filter(owner_id=request.user.id)
    user_post_address_detail = UserPostAddressDetailForm(request.POST or None,request.user)#
    print('user_post_address_detail.choices[0][0]=',user_post_address_detail.choices[0][0])
    if request.method == 'POST':
        if user_post_address_detail.is_valid():
            PostAddress_id = user_post_address_detail.cleaned_data.get('PostAddress_id')
            print("PostAddress_id=",PostAddress_id)
            # Todo:save to database
            post_address =PostAddress.objects.filter(owner_id=request.user.id,id=PostAddress_id)
            print("postAddressesUser=",postAddressesUser)
            print("post_address=",post_address)
            print("post_address=",post_address[0].address)
            print("post_address.id=",post_address[0].id)
            print("order.id=",order.id)

            # post_address_detail = PostAddressDetail.objects.filter(
            #     # addressSelected = 1,
            #     # isResive =False,
            #     # OrderDetailSelected =64,
            # )


            # post_address_detail = post_address.postaddressdetail_set.create(

            post_address_detail = PostAddressDetail.objects.filter(
                                OrderDetailSelected =order,
                                ).first()
            print('post_address_detail=', post_address_detail)

            if post_address_detail is None:
                post_address_detail = PostAddressDetail.objects.create(
                    addressSelected = post_address[0],
                    OrderDetailSelected =order,
                    isResive =False,
                    ) 
            else:
                post_address_detail.addressSelected = post_address[0]
                post_address_detail.save()
                print('post_address_detail.addressSelected=', post_address_detail.addressSelected)


            


    contex ={
        'user_post_address_detail': user_post_address_detail,
        'postAddressesUser' : postAddressesUser,
        'zipee' : zip(user_post_address_detail.choices,postAddressesUser),
        
    }
    return render(request ,'add_userAdressDetail.html',contex)