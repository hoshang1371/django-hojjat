import datetime
from django.db import models
# from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    email = models.EmailField(unique=True,verbose_name="ایمیل")
    codeVarifySms = models.CharField( max_length=5,blank = True, null = True,verbose_name='کد تایید پیامکی')
    codeVarifySmsDate = models.DateTimeField(blank = True, null = True,verbose_name='زمان تایید پیامکی')
    # is_author = models.BooleanField(default=False,verbose_name="ok")



# Create your models here.
class UserData(models.Model):
    user  = models.OneToOneField(
        User ,
        on_delete=models.CASCADE,
    )
    choiceField =models.CharField(blank = True, null = True, max_length=10, verbose_name=' عنوان اجتماعی ')
    SAL =models.CharField(blank = True, null = True, max_length=10, verbose_name='سال تولد ')
    MAH =models.CharField(blank = True, null = True, max_length=10, verbose_name=' ماه تولد ')
    ROZ =models.CharField(blank = True, null = True, max_length=10, verbose_name=' روز تولد ')

#order.orderdetail_set.create(product_id=product.id, price=product.price ,count=count)
    class Meta:
        verbose_name = ' اطلاعات شخصی کاربران '
        verbose_name_plural=' اطلاعات شخصی '

    def __str__(self):
        return self.user.get_full_name()




