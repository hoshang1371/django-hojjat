# Generated by Django 4.0.4 on 2022-09-17 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spad_eshop_products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='عنوان')),
                ('slug', models.SlugField(verbose_name='عنوان در url')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('active', models.BooleanField(default=True, verbose_name='فعال / غیر فعال')),
                ('products', models.ManyToManyField(blank=True, to='spad_eshop_products.product', verbose_name='محصولات')),
            ],
            options={
                'verbose_name': 'برچسب / تگ',
                'verbose_name_plural': 'برچسب ها / تگ ها',
            },
        ),
    ]
