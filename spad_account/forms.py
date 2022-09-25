from django import forms
from django.forms.widgets import PasswordInput, TextInput
# from django.contrib.auth.models import User
from django.core import validators
from spad_account.models import User

from captcha.fields import CaptchaField, CaptchaTextInput

from django.contrib.auth.forms import UserCreationForm

# from captcha import CaptchaTextInput

# BIRTH_YEAR_CHOICES = ['1371', '1372', '1373', '1374', '1375']
# BIRTH_MOUNTS_CHOICES = ['5', '4', '3', '2', '1']
# BIRTH_MOUNT_CHOICES = ['فروردین', 'ادیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']

# FAVORITE_COLORS_CHOICES = [
#     ('blue', 'Blue'),
#     ('green', 'Green'),
#     ('black', 'Black'),
# ]

# class CaptchaTestForm(forms.Form):
#     # myfield = AnyOtherField()
#     captcha = CaptchaField()

CHOICES = [('1', 'اقا'), ('2', 'خانم')]
SAL = (())
MAH = (
        ('فروردین' , 'فروردین'),
        ('اریبهشت' , 'اریبهشت'),
        ('خرداد' , 'خرداد'),
        ('تیر' , 'تیر'),
        ('مرداد' , 'مرداد'),
        ('شهریور' , 'شهریور'),
        ('مهر' , 'مهر'),
        ('آبان' , 'آبان'),
        ('آذر' , 'آذر'),
        ('دی' , 'دی'),
        ('بهمن' , 'بهمن'),
        ('اسفند' , 'اسفند'),
    )
ROZ = (())

for i in range(1300,1500):
    SAL = SAL + ((f'{i}',f'{i}'),)

for j in range(1,31):
    ROZ = ROZ + ((f'{j}',f'{j}'),)


# from django import forms
# from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
# from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime



#from django_jalali.db import models as jmodels
# from django_jalali.admin.filters import JDateFieldListFilter

# you need import this for adding jalali calander widget
# import django_jalali.admin as jadmin

class EditUserForm(forms.Form):

    first_name= forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفاً نام  خود را وارد نمایید ', 'class' : 'form-control rtl'}),
        label=' نام  '
    )

    last_name= forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفاً نام خانوادگی خود را وارد نمایید ', 'class' : 'form-control rtl'}),
        label=' نام خانوادگی '
    )

    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES,
                                    label=' عنوان اجتماعی ')

    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'ایمیل',"class":"rtl"}),
        label=' ایمیل',
        validators=[
            validators.EmailValidator(' ایمیل وارد شده معتبر نمی باشد ')
        ]
    )

    SAL = forms.ChoiceField(choices=SAL)

    MAH = forms.ChoiceField(choices=MAH)

    ROZ = forms.ChoiceField(choices=ROZ)

    password_now = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'گذرواژه فعلی',"class":"rtl password"}),
        label=' گذرواژه فعلی',
    )

    password_new = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'گذرواژه فعلی',"class":"rtl password"}),
        label=' رمز عبور جدید ',
    )

    password_accept = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'گذرواژه فعلی',"class":"rtl password"}),
        label=' رمز عبور جدید ',
    )

    def clean_password_accept(self):
        password_new = self.cleaned_data.get('password_new')
        password_accept = self.cleaned_data.get('password_accept')

        if password_new != password_accept:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')

        return password_new
    # password_accept = forms.CharField(
    #     widget=forms.TextInput(attrs={'placeholder':' تاییدیه ',"class":"rtl"}),
    #     label=' تاییدیه ',
    #     validators=[
    #         validators.EmailValidator(' تاییدیه ')
    #     ]
    # )

    # birth_date= forms.DateField(label='تاریخ تولد', years=BIRTH_YEAR_CHOICES
    #                             widget=forms.SelectDateWidget), month=BIRTH_MOUNT_CHOICES

    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    # favorite_colors = forms.MultipleChoiceField(
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=FAVORITE_COLORS_CHOICES,
    # )



class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفاً نام کاربری خود را وارد نمایید', 'class':'rtl '}),
        label=' نام کاربری '
    )

    password = forms.CharField(
        widget= forms.PasswordInput(attrs={'placeholder':'کلمه ی عبور', 'class':'password rtl'}),
        label=' کلمه ی عبور '
    )

    # def clean_user_name(self):
    #     user_name = self.cleaned_data.get('username')
    #     is_exsist_user = User.objects.filter(username = user_name).exists()
        
    #     if not is_exsist_user:
    #         raise forms.ValidationError('کاربری با مشخصات وارد شده ثبت نام نکرده است')

            
    #     return user_name

class CustomCaptchaTextInput(CaptchaTextInput):
    template_name = 'captcha/captcha_field.html'
    # def __init__(self, *arg,**kwargs):
    #     super.__init__(self, *arg,**kwargs)
    #     for field in self.widgets:
    #         print(field)

class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'نام کاربری',"class":"rtl","tabindex":"1"}),
        label=' نام کاربری ',
        # validators=[
        #     validators.MaxLengthValidator(limit_value=20,
        #                                  message='تعداد کارکتر های وارد شده نمی تواند بیشتر از 20 باشد'),
        #     validators.MinLengthValidator(4, 'تعداد کارکتر های وارد شده نمی تواند کمتر از 4 باشد')
        # ]
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'ایمیل',"class":"rtl","tabindex":"2"}),
        label=' ایمیل',
        validators=[
            validators.EmailValidator(' ایمیل وارد شده معتبر نمی باشد ')
        ]
    )

    password = forms.CharField(
        widget= forms.PasswordInput(attrs={'placeholder':'کلمه ی عبور',"class":"rtl password","tabindex":"3"}),
        label=' کلمه ی عبور '
    )

    re_password = forms.CharField(
        widget= forms.PasswordInput(attrs={'placeholder':'تکرار کلمه ی',"class":"rtl password","tabindex":"4"}),
        label=' تکرار کلمه ی عبور  '
    )
    #ToDO
    captcha = CaptchaField(
        widget=CustomCaptchaTextInput
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        
        if is_exists_user_by_email:
            raise forms.ValidationError(' ایمیل وارد شده تکراری می باشد ')

        # if len(email) > 20:
        #     raise forms.ValidationError(' تعداد کارکتر های وارد شده باید کمتر از 20 باشد ')

        return email


    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exists_user_by_username = User.objects.filter(username=user_name).exists()

        if is_exists_user_by_username:
            raise forms.ValidationError('این کاربر قبلاً ثبت نام کرده است')

        return user_name


    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')

        return password


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'placeholder': 'ایمیل خود را وارد کنید',
        "class":"rtl",
        "tabindex":"2"
        }))


class UserSetPasswordForm(SetPasswordForm):
    # def __init__(self, *args, **kwargs):
    #     super(SetPasswordForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder': ' پسوورد خود را وارد کنید',
        "class":"rtl",
        "tabindex":"2"
        }))

    new_password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder': ' تکرار پسوورد خود راوارد کنید ',
        "class":"rtl",
        "tabindex":"2"
        }))