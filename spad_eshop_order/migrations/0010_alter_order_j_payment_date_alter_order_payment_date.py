# Generated by Django 4.1.7 on 2023-03-31 16:54

from django.db import migrations, models
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('spad_eshop_order', '0009_order_j_payment_date_alter_order_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='j_payment_date',
            field=django_jalali.db.models.jDateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='تاریخ ایجاد سبد شمسی'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='تاریخ ایجاد سبد'),
        ),
    ]
