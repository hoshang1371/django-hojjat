# Generated by Django 4.0.4 on 2022-10-20 12:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spad_eshop_order', '0005_remove_order_j_payment_date_alter_order_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='تاریخ پرداخت'),
        ),
    ]
