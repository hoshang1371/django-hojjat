from django import forms
from django.contrib.auth.models import User
from django.core import validators

class CustomersCommentsForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفاً نام و نام خانوادگی', 'class':'rtl'}),
        label = 'نام و نام خوانوادگی',
        validators=[
            validators.MaxLengthValidator(150, 'نام و نام خانوادگی شما نمی تواند بیشتر از 150 کارکتر باشد')
            ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':'لطفاً ایمیل خود را وارد نمایید', 'class':'rtl'}),
        label = ' ایمیل ',
                validators=[
            validators.MaxLengthValidator(100, ' ایمیل شما نمی تواند بیشتر از 100 کارکتر باشد')
            ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفاً عنوان خود را وارد نمایید', 'class':'rtl'}),
        label = ' عنوان ',
        validators=[
            validators.MaxLengthValidator(200, ' عنوان شما نمی تواند بیشتر از 200 کارکتر باشد ')
            ]
    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':'لطفاً متن خود را وارد نمایید', 
                                "class":"rtl form-control ",'rows':8, 'cols':15}),
        label = ' متن پیام ',
    )

