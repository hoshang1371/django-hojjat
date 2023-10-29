from django.http import JsonResponse
from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from requests import Response
from post_information.forms import PaymentMethod, RegisterPaymentInformationForm, UserPostAddressDetailForm,AddAddress,Country,CarrierChoices
from post_information.models import PaymentMethodeDetail, PostAddressDetail, PostPrice,PostAddress,Carrier_CHOICES
from spad_account.models import User

from spad_eshop_order.models import Order, OrderDetail
from spad_eshop_settings.models import SiteSetting

from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication

from extentions.sendSmsRandom import random_with_N_digits,sendSmsForVarifyAddress,sendSms
from extentions import globalValue,pdf
from django.http import HttpResponse

# from extentions import sendSmsRandom
import threading

from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

from spad_account.token import account_activation_token

# from rest_framework.response import Response as resResponse
from django.contrib import messages
import datetime 
# t1 = threading.Thread(target=sendSmsForVarifyAddress, args=(10,))
# stop_threads_sendSmsVarify =False
# code=''
# print('codeGlobal=',globalValue.code)
@login_required(login_url='/login')
def post_order(request):
    postAddressesUser = PostAddress.objects.filter(owner_id=request.user.id)
    #! forms of postaddress
    user_post_address_detail = UserPostAddressDetailForm(request.POST or None,request.user)#
    # if request.method == 'POST':
    if user_post_address_detail.is_valid():
        product_id = user_post_address_detail.cleaned_data.get('PostAddress_id')
        print('product_id=',product_id)
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

# datetime.datetime.now(datetime.timezone.utc).timestamp()-h.codeVarifySmsDate.timestamp()
@login_required(login_url='/login')
def post_add_address(request):

    user = User.objects.get(id=request.user.id)

    add_address = AddAddress(request.POST or None)
    # global stop_threads_sendSmsVarify
    # stop_threads_sendSmsVarify = True

    if request.method == 'POST':
        if add_address.is_valid():
            first_name_for_post = add_address.cleaned_data.get('first_name_for_post')
            last_name_for_post = add_address.cleaned_data.get('last_name_for_post')
            Country_for_post = add_address.cleaned_data.get('Country_for_post')
            City_for_post = add_address.cleaned_data.get('City_for_post')
            Address_for_post = add_address.cleaned_data.get('Address_for_post')
            phone_number_for_post = add_address.cleaned_data.get('phone_number_for_post')
            global mobile_phone_number_for_post
            mobile_phone_number_for_post = add_address.cleaned_data.get('mobile_phone_number_for_post')
            check_mobile_phone_number_for_post = add_address.cleaned_data.get('check_mobile_phone_number_for_post')
            post_code_for_post = add_address.cleaned_data.get('post_code_for_post')
            # print(first_name_for_post)
            # print(last_name_for_post)
            # print('Country_for_post',Country_for_post)
            # print('Country',Country[0][1])
            # print(City_for_post)
            # print(Address_for_post)
            # print(phone_number_for_post)
            # print(mobile_phone_number_for_post)
            # print('check_mobile_phone_number_for_post',check_mobile_phone_number_for_post)
            # # global code
            # print('is it',globalValue.code)

            # user.codeVarifySmsDate = datetime.datetime.now(datetime.timezone.utc)
            deffTime =int(datetime.datetime.now(datetime.timezone.utc).timestamp()-user.codeVarifySmsDate.timestamp())

            if(deffTime < 120):
            #! check mobile number
                if user.codeVarifySms == check_mobile_phone_number_for_post:
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
                            isCorrect_mobile_phone_number = True
                            )
                    # print("redirect")
                    return redirect('/post_info/سفارش')
            
            messages.success(request, 'کد ارسالی صحیح نمیباشد')
            return redirect('/post_info/post_add_address')      


        
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

#!send code for varify mobile address
class send_code_for_varify_mobile_address(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication, )

    def post(self, request, *args, **kwargs):

        user = User.objects.get(id=request.user.id)
        # print('post')
        # print(self.request.user)
        # print(request.data)
        mobNumber =request.data.get('mobNum')
        # print(request.data.get('mobNum'))
        if mobNumber=='':
            # TODO : ارور برای وارد کردن شماره موبایل
            # messages.success(request, 'لطفاً شماره موبایل را وارد کنید.')
            # print("not ok")
            return JsonResponse({"mobNum": "not ok"})
        

        # globalValue.code = ''

        # globalValue.code = random_with_N_digits(5)
        user.codeVarifySms = random_with_N_digits(5)
        user.codeVarifySmsDate = datetime.datetime.now(datetime.timezone.utc)
        print(user)
        user.save()

        sendSms(user.codeVarifySms,mobNumber)


        
        # print('send_code_for_varify_mobile_addressCode=',globalValue.code)
        # global stop_threads_sendSmsVarify
        # stop_threads_sendSmsVarify = False
        # sendSmsVarify = threading.Thread(
        #         target=sendSmsForVarifyAddress, 
        #         args=(
        #             self.request.user,
        #             lambda : stop_threads_sendSmsVarify,
        #             )
        #         )
        # sendSmsVarify.start()

        return JsonResponse({'mobNum':'ok'})

    def get(self, request, *args, **kwargs):
        # print('nanat o sag gaiid')
        print(self.request.user)
        print(request.body)
        # global code
        # code = random_with_N_digits(5)
        # print('send_code_for_varify_mobile_addressCode=',code)
        # globalValue.code = ''
        globalValue.code = random_with_N_digits(5)
        print('send_code_for_varify_mobile_addressCode=',globalValue.code)

        global stop_threads_sendSmsVarify
        # stop_threads_sendSmsVarify = True
        stop_threads_sendSmsVarify = False
        # print(stop_threads_sendSmsVarify)
        sendSmsVarify = threading.Thread(
                target=sendSmsForVarifyAddress, 
                args=(
                    self.request.user,
                    lambda : stop_threads_sendSmsVarify,
                    )
                )
        sendSmsVarify.start()
        # stop_threads_sendSmsVarify = True

        return JsonResponse({'foo':'bar'})
    
@login_required(login_url='/login')
def edit_post_add_address(request, pk):
    print('pk')
    print(pk)
    user = User.objects.get(id=request.user.id)


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

    if request.method == 'POST':
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
            deffTime =int(datetime.datetime.now(datetime.timezone.utc).timestamp()-user.codeVarifySmsDate.timestamp())
            if(deffTime < 120):

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

            messages.success(request, 'کد ارسالی صحیح نمیباشد')
            return redirect('/post_info/post_add_address')    
        
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
    # postAddressesUser = PostAddress.objects.filter(owner_id=request.user.id)
    user_post_address_detail = UserPostAddressDetailForm(request.POST or None,request.user)#
    carriersChoices = CarrierChoices(request.POST or None,request.user)
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
                print('post_address_detail.addressSelected=', post_address_detail.addressSelected.id)




    # order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
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

    contex ={
        'username' : username,
        'setting': site_setting,
        # 'user_post_address_detail': user_post_address_detail,
        # 'postAddressesUser' : postAddressesUser,
        'carriersChoices' : carriersChoices['Carrier_field'],

        'Total_price_for_all_product_buy' : Total_price_for_all_product_buy,
        'post_price': post_price.price,
        'count_off_all_product': count_off_all_product,

        # 'zipee' : zip(user_post_address_detail.choices,postAddressesUser),
        
    }
    return render(request ,'add_userAdressDetail.html',contex)


@login_required(login_url='/login')
def paymentMethod(request):
    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    carriersChoices = CarrierChoices(request.POST or None,request.user)
    paymentMethod = PaymentMethod(request.POST or None,request.user)


    if request.method == 'POST':        
        if carriersChoices.is_valid():
            Carrier_field = carriersChoices.cleaned_data.get('Carrier_field')
            print(Carrier_field)

            post_address_detail = PostAddressDetail.objects.filter(
                                OrderDetailSelected =order,
                                ).first()
            print('post_address_detail=', post_address_detail)

            post_address_detail.carrierDetails = Carrier_field

            post_address_detail.save()

            print('post_address_detail.carrierDetails',post_address_detail.carrierDetails)


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


    username = request.user.username
    site_setting = SiteSetting.objects.first()

    contex={
        'username' : username,
        'setting': site_setting,
        # 'user_post_address_detail': user_post_address_detail,
        # 'postAddressesUser' : postAddressesUser,
        'paymentMethods' : paymentMethod['paymentMethod_field'],
        'paymentMethod_isTermsAndRules' : paymentMethod['isTermsAndRules'],

        'Total_price_for_all_product_buy' : Total_price_for_all_product_buy,
        'post_price': post_price.price,
        'count_off_all_product': count_off_all_product,
    }
    return render(request ,'paymentMethod.html',contex)

from django.utils.html import strip_tags

@login_required(login_url='/login')
def cartToCartPeyment(request):



    username = request.user.username
    site_setting = SiteSetting.objects.first()
    user = User.objects.filter(id=request.user.id)


    

    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    # print('kir khar')
    # print('order=',order)
    # if order[0] is None:
    #  print('kir khar')
    # order_details = OrderDetail.objects.get_queryset().filter(order=order)
    paymentMethod = PaymentMethod(request.POST or None,request.user)

    post_address_detail = PostAddressDetail.objects.filter(
                        OrderDetailSelected =order,
                        ).first()
    
    # print('order_details=',order_details)
    
    # print('post_address_detail.carrierDetails=',post_address_detail.carrierDetails)
    # print('type=',type(post_address_detail.carrierDetails))
    # print('Carrier_CHOICES=',Carrier_CHOICES[int(post_address_detail.carrierDetails)-1][1])
    order_partials_buy = order.orderdetail_set.all()

    post_price = PostPrice.objects.filter().first()
    #order_partials = OrderDetail.objects.all()
    Total_price_for_all_product_buy =0
    count_off_all_product =0

    if request.method == 'POST':
        if paymentMethod.is_valid():
            PaymentMethod_field = paymentMethod.cleaned_data.get('paymentMethod_field')
            isTermsAndRules_field = paymentMethod.cleaned_data.get('isTermsAndRules')
            # print('PaymentMethod_field',PaymentMethod_field)
            # print('isTermsAndRules_field',isTermsAndRules_field)

            paymentMethodeDetail = PaymentMethodeDetail.objects.filter(
                    OrderDetailSelected =order,
                    ).first()
            print('paymentMethodeDetail=',paymentMethodeDetail)

            if paymentMethodeDetail is None:
                paymentMethodeDetail = PaymentMethodeDetail.objects.create(
                    OrderDetailSelected =order,
                    PaymentDetails=PaymentMethod_field,
                    isTermsAndRules =isTermsAndRules_field,
                    ) 
                
            else:
                paymentMethodeDetail.PaymentDetails=PaymentMethod_field
                paymentMethodeDetail.isTermsAndRules=isTermsAndRules_field
                paymentMethodeDetail.save()



        # #* factor baraye email
        #     for order_partial in order_partials_buy:
        #         count_off_all_product = count_off_all_product+1
        #         Total_price_for_each_product_buy = order_partial.count * order_partial.price
        #         Total_price_for_all_product_buy = Total_price_for_all_product_buy + Total_price_for_each_product_buy
        #     contex = {
        #         'order_details' : order_partials_buy,
        #         'total_price_ofProduct' : Total_price_for_all_product_buy,
        #         'post_price': post_price.price,
        #     }   

        #     pdf_ = pdf.html_to_pdf(request,'buyFactor.html',contex )

        #     return HttpResponse(pdf_, content_type='application/pdf') 
        #! 
            current_site = get_current_site(request)
        
            mail_subject = ' فاکتور '
            message = render_to_string('acc_sendOrderDitails.html', {
                'user': request.user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(request.user.pk)),
                'token':account_activation_token.make_token(request.user),
                'order': order,
                
            })
            email = EmailMessage(
                    mail_subject, message, to=[user[0].email]
                )
            
            # email.content_subtype = 'html'
            #! فعال شود.
            email.send()

            print('every thing ok')
    for order_partial in order_partials_buy:
        count_off_all_product = count_off_all_product+1
        Total_price_for_each_product_buy = order_partial.count * order_partial.price
        Total_price_for_all_product_buy = Total_price_for_all_product_buy + Total_price_for_each_product_buy
    contex = {
        'order': order,
        'order_details' : order_partials_buy,
        'username' : username,
        'setting': site_setting,

        'total_price_ofProduct' : Total_price_for_all_product_buy,
        'Total_price_for_all_product_buy' : Total_price_for_all_product_buy,
        'post_price': post_price.price,
        'count_off_all_product': count_off_all_product,

        'carrierDetails' : Carrier_CHOICES[int(post_address_detail.carrierDetails)-1][1],

        'user' : user[0],

    }
    return render(request ,'cartToCartPeyment.html',contex)
    


@login_required(login_url='/login')
def pdf_factor(request,pk):
    # order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    order = Order.objects.filter(owner_id= request.user.id,id=pk)
    # print('order1=',order1[0])
    # print('order=',order.first())
    # print('kir khar') 
    if order.first() is None:
        return redirect('/login')

    order_partials_buy = order[0].orderdetail_set.all()
    post_price = PostPrice.objects.filter().first()

    #* factor baraye email
    count_off_all_product =0
    Total_price_for_all_product_buy=0
    for order_partial in order_partials_buy:
        count_off_all_product = count_off_all_product+1
        Total_price_for_each_product_buy = order_partial.count * order_partial.price
        Total_price_for_all_product_buy = Total_price_for_all_product_buy + Total_price_for_each_product_buy
    contex = {
        'order_details' : order_partials_buy,
        'total_price_ofProduct' : Total_price_for_all_product_buy,
        'post_price': post_price.price,
    }   

    pdf_ = pdf.html_to_pdf(request,'buyFactor.html',contex )

    return HttpResponse(pdf_, content_type='application/pdf') 




@login_required(login_url='/login')
def RegisterPaymentInformation(request,pk):
    username = request.user.username
    site_setting = SiteSetting.objects.first()
    register_payment_information = RegisterPaymentInformationForm(request.POST or None)

    order = Order.objects.filter(owner_id= request.user.id,id=pk)
    if order.first() is None:
        return redirect('/login')
    paymentMethodeDetail = PaymentMethodeDetail.objects.filter(
                    OrderDetailSelected =order[0],
            ).first()
    print('paymentMethodeDetail=',paymentMethodeDetail)

    if register_payment_information.is_valid():
        register_payment = register_payment_information.cleaned_data.get('register_payment')
        print(register_payment)
        paymentMethodeDetail.peymentCode=register_payment
        paymentMethodeDetail.save()
        return redirect('/post_info/cartToCartPeyment')
    contex = {
        'username' : username,
        'setting': site_setting,
        'register_payment_information': register_payment_information
    }
    return render(request ,'RegisterPaymentInformation.html',contex)