from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordContextMixin
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model, authenticate, logout
from django.core.exceptions import ObjectDoesNotExist, ValidationError
#from django.core.exceptions import ValidationError
from django.views.generic.edit import FormView
from django.utils.encoding import force_bytes,force_str
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from post_information.models import PostAddress, PostAddressDetail, PostPrice
from spad_account.serializer import PostAddressDeleteListOfBuySerializer

from spad_eshop_settings.models import SiteSetting#, force_text

from spad_eshop_order.models import Order, OrderDetail

from .token import account_activation_token
from django.core.mail import EmailMessage
#from django.contrib.auth.forms import PasswordChangeForm
from .forms import LoginForm, RegisterForm, EditUserForm, ChangePass
# from django.contrib.auth.models import User
from spad_account.models import User

#import  django.contrib.auth.hashers

from django.contrib.auth.password_validation import validate_password

from django.http import HttpResponse
from .models import UserData

from jalali_date import datetime2jalali, date2jalali

from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication


def login_user(request):
    # if request.user.is_authenticated:
    #     return redirect('/')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        # print(user_name)
        # print(password)
        # print(user)
        # print(login_form.cleaned_data)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('user_name', 'کاربری با مشخصات وارد شده یافت نشد')
    username = request.user.username
    site_setting = SiteSetting.objects.first()
    context = {
        'username' : username,
        'setting': site_setting,
        'login_form': login_form
    }
    return render(request, 'account/login.html', context)



def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    # if request.POST:
    register_form = RegisterForm(request.POST or None)
    
    # form = CaptchaTestForm(request.POST)

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        # re_password = register_form.cleaned_data.get('re_password')
        # email = register_form.cleaned_data.get('email')
        captcha =register_form.cleaned_data.get('captcha')

        user = User.objects.create_user(username=user_name,email=email,password=password,is_active = False)
        print(user.pk)
        # user = User.objects.filter(username=user_name)
        current_site = get_current_site(request)

        mail_subject = 'فعال سازی اکانت'
        message = render_to_string('account/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
                
            })
        to_email = register_form.cleaned_data.get('email')
        email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
        email.send()
        return HttpResponse("لینک فعال سازی یه ایمیل شما ارسال شد <a href='/login'> ورود </a>")
        # return redirect('/login')

    username = request.user.username
    site_setting = SiteSetting.objects.first()
    context = {
        'username' : username,
        'setting': site_setting,
        'register_form': register_form,
        #'Captcha' : captcha
    }
    return render(request, 'account/register.html', context)

def log_out(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def UnpaidOrder(request):
    orders = Order.objects.filter(owner_id= request.user.id  ,is_paid=False)
    user = User.objects.filter(id=request.user.id)

    context ={
        'orders' : orders,
        'user' : user[0]
    }
    return render(request, 'account/UnpaidOrder.html',context)

@login_required(login_url='/login')
def historyOrder(request):
    orders = Order.objects.filter(owner_id= request.user.id).all()
    user = User.objects.filter(id=request.user.id)

    context ={
        'orders':orders,
        'user' : user[0]
    }
    return render(request, 'account/HistoryOrder.html',context)

@login_required(login_url='/login')
def addresses(request):
    postAddressesUser = PostAddress.objects.filter(owner_id=request.user.id)
    user = User.objects.filter(id=request.user.id)

    context ={
        'postAddressesUser' : postAddressesUser,
        'user' : user[0]
    }
    return render(request, 'account/addresses.html',context)

@login_required(login_url='/login')
def editOrder(request,pk):
    order = Order.objects.filter(owner_id= request.user.id,id=pk)
    user = User.objects.filter(id=request.user.id)
    order_details = OrderDetail.objects.get_queryset().filter(order__id=pk,order__owner_id=request.user.id)
    total_price = 0
    for orderDetail in order_details:
        total_price = total_price + (orderDetail.price * orderDetail.count)

    post_price = PostPrice.objects.filter().first()

    post_address_detail = PostAddressDetail.objects.filter(
                                OrderDetailSelected =order[0],
                                ).first()
    
    # postAddressesUser = PostAddress.objects.filter(owner_id=request.user.id)

    # print('order',order)
    print('post_address_detail=', post_address_detail)

    # print('post_address_detail=', post_address_detail.carrierDetails)

    # print('post_address_detail=', type(post_address_detail.carrierDetails))

    # print('post_address_detail=', post_address_detail.addressSelected.post_code)
    
    # print(order_details[0].product.title)
    # print(order_details[0].product.number)
    # print(order[0])
    context ={
        'order': order[0],
        'user' : user[0],
        'order_details' : order_details,
        'total_price_ofProduct' : total_price,
        'post_price' : post_price.price,
        'post_address_detail' : post_address_detail,
    }
    return render(request, 'account/details_order.html',context)

#! delete PostAddress detail
class PostAddress_delete_list_of_buy(DestroyAPIView):
    queryset = PostAddress.objects.all()
    #queryset = Order.objects.filter(owner_id= request.user.id, is_paid=False).first()
    #queryset = OrderDetail.objects.all()
    serializer_class = PostAddressDeleteListOfBuySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (SessionAuthentication, )

@login_required(login_url='/login')
def edit_user_profile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
#    user_data = UserData.objects.get(id=user_id)

#    fm = PasswordChangeForm()

    # userPassword = User.objects.get(userPassword)
    # userdata = UserData.objects.all()
    #.get_queryset().get(id=detail_id, order__owner_id=request.user.id)
    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')

    edit_user_form = EditUserForm(request.POST or None)
    if request.method == 'POST':
        if edit_user_form.is_valid():
            first_name = edit_user_form.cleaned_data.get('first_name')
            last_name = edit_user_form.cleaned_data.get('last_name')
            email = edit_user_form.cleaned_data.get('email')
            choice_field = edit_user_form.cleaned_data.get('choice_field')
            SAL = edit_user_form.cleaned_data.get('SAL')
            MAH = edit_user_form.cleaned_data.get('MAH')
            ROZ = edit_user_form.cleaned_data.get('ROZ')
            # password_now = edit_user_form.cleaned_data.get('password_now')
            # password_new = edit_user_form.cleaned_data.get('password_new')
            # password_accept = edit_user_form.cleaned_data.get('password_accept')



            # check = user.check_password(password_now)
            # if check == True:
            #     if password_new == password_accept:
            #         user.set_password(password_new)


            user.first_name = first_name
            user.last_name = last_name
            # if user.userdata.choiceField is None:
            #     UserData.objects.create(user=user,choiceField=choice_field)
            # else:
            #     user.userdata.choiceField = choice_field
            try:
                user.userdata.choiceField = choice_field
            except ObjectDoesNotExist:
                UserData.objects.create(user=user,choiceField=choice_field)
            
            try:
                user.userdata.SAL = SAL
            except ObjectDoesNotExist:
                UserData.objects.create(user=user, SAL=SAL)

            try:
                user.userdata.MAH = MAH
            except ObjectDoesNotExist:
                UserData.objects.create(user=user, MAH=MAH)

            try:
                user.userdata.ROZ = ROZ
            except ObjectDoesNotExist:
                UserData.objects.create(user=user, ROZ=ROZ)

            user.save()
            user.userdata.save()

            return redirect('/')
            
    username = request.user.username
    site_setting = SiteSetting.objects.first()
    
    
    contex = {
        'username' : username,
        'setting': site_setting,
        'edit_form' : edit_user_form
        }
    
    return render(request,'account/edit_account.html', contex)


# class ChildPasswordResetView(PasswordContextMixin, FormView):
#     template_name = "registration/password_reset_form.html"

# def my_view(request):
# 	jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
# from django.utils.encoding import force_bytes, force_text


@login_required(login_url='/login')
def change_pass(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)

    change_pass = ChangePass(request.POST or None)
    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')

    if request.method == 'POST':
        if change_pass.is_valid():
            password_now = change_pass.cleaned_data.get('password_now')
            password_new = change_pass.cleaned_data.get('password_new')
            password_accept = change_pass.cleaned_data.get('password_accept')
            check = user.check_password(password_now)
            if check == True:
                if password_new == password_accept:
                   user.set_password(password_new)
                   user.save()
                   return redirect('/')

    
    username = request.user.username
    site_setting = SiteSetting.objects.first()
    
    contex = {
        'username' : username,
        'setting': site_setting,
        'change_pass' : change_pass
        }
    
    return render(request,'account/change_pass.html', contex)

def activate(request, uidb64, token):
    try:
        # uid = force_text(urlsafe_base64_decode(uidb64))
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('home')
        return HttpResponse('اکانت شما با موفقیت فعال شد. برای <a href="/login"> ورود </a>')
    else:
        return HttpResponse('لینک فعال سازی منقضی شده است!<a href="/register"> دوباره امتحان کنید </a>')
