from django.db import models

# from django.db import models

class ProductCategoryCat(models.Model):
    title = models.CharField(max_length=150 ,verbose_name='عنوان', null=True, blank=True)
    #name = models.CharField(max_length=150 ,verbose_name='عنوان در url')
    #catCategory = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'دسته بندی اصلی'
        verbose_name_plural = 'دسته بندی ها اصلی'

    def __str__(self):
        return self.title

class ProductCategory(models.Model):
    title = models.CharField(max_length=150 ,verbose_name='عنوان')
    name = models.CharField(max_length=150 ,verbose_name='عنوان در url')
    catCategory = models.ForeignKey(ProductCategoryCat, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title

