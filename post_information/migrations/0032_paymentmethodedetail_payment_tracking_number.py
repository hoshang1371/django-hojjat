# Generated by Django 4.1.7 on 2023-08-11 12:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_information', '0031_alter_postaddressdetail_orderdetailselected'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmethodedetail',
            name='payment_tracking_number',
            field=models.CharField(blank=True, max_length=25, null=True, validators=[django.core.validators.RegexValidator(regex='^\\d{25}$')], verbose_name='شماره پیگیری'),
        ),
    ]
