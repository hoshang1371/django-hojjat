# Generated by Django 4.1.7 on 2023-08-11 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spad_eshop_order', '0013_order_payment_tracking_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_tracking_number',
        ),
    ]
