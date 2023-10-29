from django.urls import path
#from django.urls.conf import include reverse_lazy
from django.contrib.auth import views

from .views import (PostAddress_delete_list_of_buy, UnpaidOrder, addresses, editOrder, historyOrder, login_user, register, log_out,
                    edit_user_profile, activate,change_pass)

from .forms import UserPasswordResetForm, UserSetPasswordForm

urlpatterns = [
    path('login', login_user,name='login'),
    path('register', register,name='register'),

    # url(r'^signup/$', views.signup, name='signup'),
    #re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',activate, name='activate'),
    path('activate/<slug:uidb64>/<slug:token>/',activate, name='activate'),
    path('log-out', log_out,name='log-out'),
    path('user', UnpaidOrder,name='user'),
    path('historyOrder', historyOrder,name='historyOrder'),
    path('addresses', addresses,name='addresses'),
    path('changePass', change_pass,name='changePass'),
    path('editOrder/<int:pk>', editOrder,name='editOrder'),
    path('user/edit', edit_user_profile),

    path('PostAddress_delete_list_of_buy/<int:pk>', PostAddress_delete_list_of_buy.as_view()),

]

urlpatterns += [

    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', views.PasswordResetView.as_view(
                    template_name='account/password_reset_form.html',
                    form_class=UserPasswordResetForm,
                    ), 
        name='password_reset'
        ),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(
                    template_name='account/password_reset_confirm.html',
                    form_class = UserSetPasswordForm
                    ), 
        name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),

]