from django.db import models

class PostPrice(models.Model):
    title = models.CharField(max_length=150, verbose_name='هزینه ارسال ')
    price = models.IntegerField(verbose_name='هزینه ی پست')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'هزینه ارسال'

    # def __str__(self):
    #     return self.title