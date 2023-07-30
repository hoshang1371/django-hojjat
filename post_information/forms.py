from django import forms

from post_information.models import PostAddress

class UserPostAddressDetailForm(forms.Form):

    # CHOICES = [('1', 'First'), ('2', 'Second'), ('3', 'three')]

    PostAddress_id = forms.ChoiceField(
        widget=forms.RadioSelect,
        # choices= CHOICES
    )
    
    # isResive = forms.BooleanField(
    #     # widget=forms.HiddenInput(),
    #     initial=True
    #     )
    
    def __init__(self, *args, **kwargs):
        user =args[1]
        postAddressesUser = PostAddress.objects.filter(owner_id=user.id)
        # postAddressesUser = PostAddress.objects.filter(owner_id=14)
        self.choices = []
        for p in postAddressesUser:
            t = (str(p.id),p.address)
            self.choices.append(t)
        super(UserPostAddressDetailForm, self).__init__(*args, **kwargs)
        self.fields['PostAddress_id'].choices =self.choices

Country = [('1', 'ایران')]

from django.core.validators import RegexValidator
phone_validator = RegexValidator(r"^\0?1?\d{9,15}$",".شماره تلفن با کد شهر وارد کنید")
mobile_phone_validator = RegexValidator(r"^\0?1?\d{9,15}$",". شماره موبایل صحیح را وارد کنید ")



class AddAddress(forms.Form):
    first_name_for_post = forms.CharField(
        widget=forms.TextInput(attrs={
             'placeholder':'لطفاً نام  خود را وارد نمایید ',
             'class' : 'form-control rtl',
             }),
        label=' نام  ',
    )

    last_name_for_post = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder':'لطفاً نام خانوادگی  خود را وارد نمایید ',
            'class' : 'form-control rtl'
            }),
        label=' نام خانوادگی '
    )

    Country_for_post = forms.ChoiceField(
        choices=Country,
        label='کشور',
        )

    City_for_post = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder':'لطفاً شهر خود را وارد نمایید ',
            'class' : 'form-control rtl'
            }),
        label=' شهر  '
    )

    Address_for_post = forms.CharField(
        widget=forms.Textarea(
        attrs={
            'placeholder':'لطفاً آدرس خود را وارد نمایید ',
        }
        ),
        label=' آدرس '
    )



    # phone_number_for_post  = forms.RegexField(
    #     regex=r'^\0?1?\d{9,15}$',
    #     # null=True, blank=True#, unique=True
    #     label=' تلفن '
    #     )

    phone_number_for_post = forms.CharField(
        widget=forms.TextInput(
        attrs={
            'placeholder':'لطفاً تلفن خود را وارد نمایید ',
            'class' : 'form-control rtl'
            },
            ),
        validators=[phone_validator],
        label=' تلفن  '
    )

    
    # mobile_phone_number_for_post  = forms.RegexField(
    #     regex=r'^\0?1?\d{9,15}$',
    #     #, unique=True
    #     label=' تلفن همراه '
    #     )

    mobile_phone_number_for_post = forms.CharField(
        widget=forms.TextInput(
        attrs={
            'placeholder':'لطفاً تلفن همراه خود را وارد نمایید ',
            'class' : 'form-control rtl mobNumber'
            },
            ),
        validators=[mobile_phone_validator],
        label=' تلفن همراه   '
    )

    check_mobile_phone_number_for_post = forms.CharField(
        widget=forms.TextInput(
        attrs={
            'placeholder':' کد تایید را وارد کنید ',
            'class' : 'form-control rtl',
            'type':'number',
            },
            ),
        label=' کد تایید موبایل '
    )
    
    post_code_for_post = forms.CharField( 
        widget=forms.TextInput(attrs={
            'placeholder':'لطفاً کد پستی خود را وارد نمایید ',
            'type':'number',
            }),
        label=' کد پستی '
        )
    

Carrier_CHOICES = (
    ('1','پست'),
    ('2','تیپاکس'),
    ('3','باربری'),
)

class CarrierChoices(forms.Form):
    # Carrier_field = forms.ChoiceField(choices = Carrier_CHOICES)
    Carrier_field = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices = Carrier_CHOICES
        )
    
payment_METHOD= (
    ('1','پرداخت توسط فیش بانکی'),
    ('2','زرین پال'),
)

class PaymentMethod(forms.Form):
    # Carrier_field = forms.ChoiceField(choices = Carrier_CHOICES)
    paymentMethod_field = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices = payment_METHOD
        )
    
    isTermsAndRules = forms.BooleanField(
        widget=forms.CheckboxInput(      
            attrs={
                'class' : 'isTermsAndRules',
            }
        )
    )

class PaymentCode(forms.Form):
    payment_code = forms.CharField(
    widget=forms.TextInput(attrs={
            'placeholder':'  ',
            # 'class' : 'form-control rtl',
            }),
    label=' نام  ',
    )