from django.db import models
from spad_account.models import User
from django.core.validators import RegexValidator

from spad_eshop_order.models import Order, OrderDetail
from django_jalali.db import models as jmodels
from django.utils.timezone import now

class PostPrice(models.Model):
    title = models.CharField(max_length=150, verbose_name='هزینه ارسال ')
    price = models.IntegerField(verbose_name='هزینه ی پست')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'هزینه ارسال'

    # def __str__(self):
    #     return self.title  Carrier details

Country_CHOICES = (
    ('iran','ایران'),
)

Carrier_CHOICES = (
    ('1','پست'),
    ('2','تیپاکس'),
    ('3','باربری'),
)

class PostAddress(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=150, verbose_name='نام')
    lastName = models.CharField(max_length=150, verbose_name='نام خانوادگی')
    country = models.CharField(max_length=20, choices=Country_CHOICES, default='iran', verbose_name='کشور')
    city = models.CharField(max_length=150, verbose_name='شهر')
    address = models.TextField(verbose_name='آدرس')
    phone_regex = RegexValidator(regex=r'^\0?1?\d{9,15}$', message="Phone number must be entered in the format: '0999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name='تلفن ثابت')
    mobile_phone_number = models.CharField(validators=[phone_regex], max_length=17, verbose_name= 'تلفن همراه')
    post_code = models.CharField(max_length=20,verbose_name='کد پستی')
    isCorrect_mobile_phone_number = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'اطلاعات پست'
        verbose_name_plural = 'اطلاعات پست'

    def __str__(self):
        return self.owner.get_full_name()
    
class PostAddressDetail(models.Model):
    # addressSelected = models.OneToOneField(PostAddress, on_delete=models.CASCADE, verbose_name=' آدرس انتخابی ')
    carrierDetails = models.CharField(max_length=20, choices=Carrier_CHOICES, default=1, verbose_name='روش ارسال')
    addressSelected = models.ForeignKey(PostAddress, on_delete=models.CASCADE, verbose_name=' آدرس انتخابی ')
    OrderDetailSelected = models.OneToOneField(Order, on_delete=models.CASCADE, verbose_name=' سبد خرید انتخابی انتخابی ')
    isResive = models.BooleanField(default=False)

    carried = jmodels.jDateTimeField(blank = True, null = True, verbose_name='تاریخ حمل شده')
    sentToShippingUnit = jmodels.jDateTimeField(blank = True, null = True, verbose_name='تاریخ ارسال شده به واحد حمل')
    collected = jmodels.jDateTimeField(blank = True, null = True, verbose_name='تاریخ جمع آوری شده')
    collecting = jmodels.jDateTimeField(blank = True, null = True, verbose_name='تاریخ در حال جمع اوری')
    Ongoing = jmodels.jDateTimeField(blank = True, null = True, verbose_name='تاریخ در دست اقدام')
    processing = jmodels.jDateTimeField(blank = True, null = True, verbose_name='تاریخ در حال پردازش')
    confirmedPayment = jmodels.jDateTimeField(blank = True, null = True, verbose_name='تاریخ پرداخت تایید شده')

    class Meta:
        verbose_name = 'اطلاعات آدرس انتخابی'
        verbose_name_plural = 'اطلاعات آدرس'

    def __str__(self):
        return self.addressSelected.address



