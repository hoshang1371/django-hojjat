# Generated by Django 4.1.7 on 2023-03-25 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spad_eshop_order', '0009_order_j_payment_date_alter_order_payment_date'),
        ('post_information', '0006_postaddressdetail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postaddressdetail',
            options={'verbose_name': 'اطلاعات آدرس انتخابی', 'verbose_name_plural': 'اطلاعات آدرس'},
        ),
        migrations.AddField(
            model_name='postaddressdetail',
            name='OrderDetailSelected',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='spad_eshop_order.orderdetail', verbose_name=' سبد خرید انتخابی انتخابی '),
            preserve_default=False,
        ),
    ]
