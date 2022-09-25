# Generated by Django 4.0.4 on 2022-09-17 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spad_eshop_products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=150, null=True, verbose_name=' نام و نام خانوادگی ')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name=' ایمیل ')),
                ('subject', models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان پیام')),
                ('text', models.TextField(blank=True, null=True, verbose_name='متن پیام')),
                ('is_ok', models.BooleanField(default=False, verbose_name='تایید شده / نشده')),
                ('ansewerText', models.TextField(blank=True, null=True, verbose_name='پاسخ متن پیام')),
                ('CommentProduct', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='spad_eshop_products.product')),
            ],
            options={
                'verbose_name': ' نظرات کاربران ',
                'verbose_name_plural': 'نظرات در مورد کالا کاربران',
            },
        ),
    ]
