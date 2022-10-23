import datetime
from django.db import models

# from django.contrib.auth.models import User
from spad_eshop_products.models import Product
from spad_account.models import User
from django.utils.timezone import now

from django_jalali.db import models as jmodels

class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(verbose_name='پرداخت شده /نشده')
    payment_date = models.DateTimeField(default=now, blank = True, null = True, verbose_name='تاریخ پرداخت')#
    j_payment_date = jmodels.jDateTimeField(default=now,blank = True, null = True, verbose_name='تاریخ پرداخت شمسی')


    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید کاربران'

    def __str__(self):
        return self.owner.get_full_name()



class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    price = models.IntegerField(verbose_name='قیمت محصول')
    count = models.IntegerField(verbose_name='تعداد')

    def get_detail_sum(self):
        return self.count * self.price

    class Meta:
        verbose_name = 'جزئیات محصول'
        verbose_name_plural = 'اطلاعات جزئیات محصولات'


    def __str__(self):
        return self.product.title
        