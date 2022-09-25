from django.db import models
from spad_eshop_products.models import Product
# from django.contrib.auth.models import User
from spad_account.models import User

class CustomerComment(models.Model):

    CommentProduct = models.ForeignKey(Product, on_delete=models.CASCADE, 
                                        null=True, blank=True)
    full_name = models.CharField(max_length=150, verbose_name=' نام و نام خانوادگی ',
                                null=True, blank=True)
    email = models.EmailField(max_length=100, verbose_name=' ایمیل ',
                                null=True, blank=True)
    subject = models.CharField(max_length=200 , verbose_name='عنوان پیام',
                                null=True, blank=True)
    text = models.TextField(verbose_name='متن پیام',
                            null=True, blank=True)
    is_ok = models.BooleanField(verbose_name='تایید شده / نشده' ,default=False)

    ansewerText = models.TextField(verbose_name='پاسخ متن پیام',
                            null=True, blank=True)
    class Meta:
        verbose_name = ' نظرات کاربران '
        verbose_name_plural='نظرات در مورد کالا کاربران'

    def __str__(self):
        return self.subject
    
