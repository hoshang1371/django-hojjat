# Generated by Django 4.1.7 on 2023-03-25 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_information', '0011_postaddressdetail_orderdetailselected'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postaddressdetail',
            name='OrderDetailSelected',
        ),
    ]