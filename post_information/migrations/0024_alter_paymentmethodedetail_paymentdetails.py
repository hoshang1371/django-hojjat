# Generated by Django 4.1.7 on 2023-07-03 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_information', '0023_paymentmethodedetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethodedetail',
            name='PaymentDetails',
            field=models.CharField(choices=[('1', 'پرداخت توسط فیش بانکی'), ('2', 'زرین پال')], default=1, max_length=20, verbose_name='روش ارسال'),
        ),
    ]
