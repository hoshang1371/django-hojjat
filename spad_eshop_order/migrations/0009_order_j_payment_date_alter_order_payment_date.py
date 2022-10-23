# Generated by Django 4.0.4 on 2022-10-20 13:06

from django.db import migrations, models
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('spad_eshop_order', '0008_remove_order_j_payment_date_alter_order_payment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='j_payment_date',
            field=django_jalali.db.models.jDateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='تاریخ پرداخت شمسی'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='تاریخ پرداخت'),
        ),
    ]
