from django.db import models

# Create your models here.
from spad_eshop_products_category.models import ProductCategory
from django.db.models import Q

import os
import random
from sorl.thumbnail import  get_thumbnail#ImageField,

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"

def upload_image_tumpnail_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products\\tumpnail\\{final_name}"

def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{final_name}"

class ProductsManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_products_by_category(self ,category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name ,active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self,query):
        lookup = (
                    Q(title__icontains=query) | 
                    Q(description__icontains=query)|
                    Q(tag__title__icontains=query))
        return self.get_queryset().filter(lookup, active=True).distinct()
from PIL import Image

from spadelc import settings 
from django_resized import ResizedImageField
import io
from django.core.files.base import ContentFile
from import_export import resources


# from PIL import Image
# from django.db.models.fields.files import ImageFieldFile
# from django.core.files.uploadedfile import InMemoryUploadedFile
# from io import BytesIO
from extentions.images import make_thumbnail

class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    code = models.CharField(max_length=150, verbose_name='کد')
    place = models.CharField(max_length=150, verbose_name='مکان کالا', null=True, blank=True)
    number = models.CharField(max_length=150, verbose_name='تعداد', null=True, blank=True)
    brand = models.CharField(max_length=150, verbose_name='برند', null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات')
    smallDescription = models.TextField(max_length=150,verbose_name='کوتاه توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    priceOff = models.IntegerField(verbose_name='قیمت تخفیف', null=True, blank=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
    image_tumpnail = models.ImageField(upload_to= upload_image_tumpnail_path, null=True, blank=True, verbose_name='تصویر_بند_انگشتی')
    #image_tumpnail = ResizedImageField(upload_to= upload_image_tumpnail_path, size=[150, 100], null=True, blank=True, verbose_name='تصویر_بند_انگشتی')
    active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    categories = models.ManyToManyField(ProductCategory, blank =True, verbose_name='دسته بندی ها')
    visit_count = models.IntegerField(default=0, verbose_name='تعداد بازدید ها')
    vige = models.BooleanField(default=False, verbose_name='ویژه / غیرویژه')
#"image": "G:'\kartmelli.jpg"
    objects = ProductsManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        # print(f"image : {self.image}")
        make_thumbnail(self.image_tumpnail, self.image, (50, 50), 'thumb')
        super(Product, self).save(*args, **kwargs)

    



class ProductGallery(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    image = models.ImageField(upload_to=upload_gallery_image_path, verbose_name='تصویر')
    product = models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name='محصول')

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'

    def __str__(self):
        return self.title