from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from post_information.forms import UserPostAddressDetailForm,AddAddress,Country
from post_information.models import PostAddressDetail, PostPrice,PostAddress

from spad_eshop_order.models import Order
from spad_eshop_settings.models import SiteSetting


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
    username = request.user.username
    site_setting = SiteSetting.objects.first()
    contex = {
        # 'order_partials_buy': order_partials_buy,
        'username' : username,
        'setting': site_setting,
        'postAddressesUser' : postAddressesUser,
        'Total_price_for_all_product_buy' : Total_price_for_all_product_buy,
        'post_price': post_price.price,
        'count_off_all_product': count_off_all_product,
        'user_post_address_detail':user_post_address_detail['PostAddress_id'],
        'zipee' : zip(user_post_address_detail['PostAddress_id'],postAddressesUser),
    }
    return render(request ,'post_order.html',contex)


@login_required(login_url='/login')
def post_add_address(request):

    add_address = AddAddress(request.POST or None)

    if add_address.is_valid():
        first_name_for_post = add_address.cleaned_data.get('first_name_for_post')
        last_name_for_post = add_address.cleaned_data.get('last_name_for_post')
        Country_for_post = add_address.cleaned_data.get('Country_for_post')
        City_for_post = add_address.cleaned_data.get('City_for_post')
        Address_for_post = add_address.cleaned_data.get('Address_for_post')
        phone_number_for_post = add_address.cleaned_data.get('phone_number_for_post')
        mobile_phone_number_for_post = add_address.cleaned_data.get('mobile_phone_number_for_post')
        post_code_for_post = add_address.cleaned_data.get('post_code_for_post')
        # print(first_name_for_post)
        # print(last_name_for_post)
        # print('Country_for_post',Country_for_post)
        # print('Country',Country[0][1])
        # print(City_for_post)
        # print(Address_for_post)
        # print(phone_number_for_post)
        # print(mobile_phone_number_for_post)
        # print(post_code_for_post)

        
        PostAddress.objects.create(
                owner_id= request.user.id,
                firstName = first_name_for_post,
                lastName = last_name_for_post,
                country = Country[0][1],
                city = City_for_post,
                address = Address_for_post,
                phone_number = phone_number_for_post,
                mobile_phone_number = mobile_phone_number_for_post,
                post_code = post_code_for_post,
                )
        # print("redirect")
        return redirect('/post_info/سفارش')      


        
    username = request.user.username
    site_setting = SiteSetting.objects.first()

    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    order_partials_buy = order.orderdetail_set.all()
    Total_price_for_all_product_buy =0
    count_off_all_product =0
    post_price = PostPrice.objects.filter().first()



    for order_partial in order_partials_buy:
        count_off_all_product = count_off_all_product+1
        Total_price_for_each_product_buy = order_partial.count * order_partial.price
        Total_price_for_all_product_buy = Total_price_for_all_product_buy + Total_price_for_each_product_buy

    contex ={
        'username' : username,
        'setting': site_setting,

        'Total_price_for_all_product_buy' : Total_price_for_all_product_buy,
        'count_off_all_product': count_off_all_product,
        'post_price': post_price.price,

        'add_address' : add_address,

    }
    return render(request ,'add_post_address.html',contex)

@login_required(login_url='/login')
def edit_post_add_address(request, pk):
    print('pk')
    print(pk)

    # PostAddress
    postData_info = PostAddress.objects.filter(id=pk)
    print(postData_info[0].firstName)
    first_name_for_edit = postData_info[0].firstName
    last_name_for_edit = postData_info[0].lastName
    Country_for_edit = postData_info[0].country
    City_for_edit = postData_info[0].city
    Address_for_edit = postData_info[0].address
    phone_number_for_edit = postData_info[0].phone_number
    mobile_phone_number_for_edit = postData_info[0].mobile_phone_number
    post_code_for_edit = postData_info[0].post_code


    add_address = AddAddress(request.POST or None,
                             initial = {
                                 'first_name_for_post': first_name_for_edit,
                                 'last_name_for_post': last_name_for_edit,
                                 'Country_for_post': Country_for_edit,
                                 'City_for_post': City_for_edit,
                                 'Address_for_post': Address_for_edit,
                                 'phone_number_for_post' : phone_number_for_edit,
                                 'mobile_phone_number_for_post' : mobile_phone_number_for_edit,
                                 'post_code_for_post' : post_code_for_edit,
                                 })

    if add_address.is_valid():
        first_name_for_post = add_address.cleaned_data.get('first_name_for_post')
        last_name_for_post = add_address.cleaned_data.get('last_name_for_post')
        Country_for_post = add_address.cleaned_data.get('Country_for_post')
        City_for_post = add_address.cleaned_data.get('City_for_post')
        Address_for_post = add_address.cleaned_data.get('Address_for_post')
        phone_number_for_post = add_address.cleaned_data.get('phone_number_for_post')
        mobile_phone_number_for_post = add_address.cleaned_data.get('mobile_phone_number_for_post')
        post_code_for_post = add_address.cleaned_data.get('post_code_for_post')
        # print(first_name_for_post)
        # print(last_name_for_post)
        # print('Country_for_post',Country_for_post)
        # print('Country',Country[0][1])
        # print(City_for_post)
        # print(Address_for_post)
        # print(phone_number_for_post)
        # print(mobile_phone_number_for_post)
        # print(post_code_for_post)

        
        postData_info.update(
                owner_id= request.user.id,
                firstName = first_name_for_post,
                lastName = last_name_for_post,
                country = Country[0][1],
                city = City_for_post,
                address = Address_for_post,
                phone_number = phone_number_for_post,
                mobile_phone_number = mobile_phone_number_for_post,
                post_code = post_code_for_post,
                )
        print("redirect")
        return redirect('/post_info/سفارش')      


        
    username = request.user.username
    site_setting = SiteSetting.objects.first()

    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    order_partials_buy = order.orderdetail_set.all()
    Total_price_for_all_product_buy =0
    count_off_all_product =0
    post_price = PostPrice.objects.filter().first()

    

    for order_partial in order_partials_buy:
        count_off_all_product = count_off_all_product+1
        Total_price_for_each_product_buy = order_partial.count * order_partial.price
        Total_price_for_all_product_buy = Total_price_for_all_product_buy + Total_price_for_each_product_buy

    contex ={
        'username' : username,
        'setting': site_setting,

        'Total_price_for_all_product_buy' : Total_price_for_all_product_buy,
        'count_off_all_product': count_off_all_product,
        'post_price': post_price.price,

        'add_address' : add_address,

    }
    return render(request ,'add_post_address.html',contex)

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
            # print("postAddressesUser=",postAddressesUser)
            # print("post_address=",post_address)
            # print("post_address=",post_address[0].address)
            # print("post_address.id=",post_address[0].id)
            # print("order.id=",order.id)

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


            
    username = request.user.username
    site_setting = SiteSetting.objects.first()

    contex ={
        'username' : username,
        'setting': site_setting,
        'user_post_address_detail': user_post_address_detail,
        'postAddressesUser' : postAddressesUser,
        'zipee' : zip(user_post_address_detail.choices,postAddressesUser),
        
    }
    return render(request ,'add_userAdressDetail.html',contex)