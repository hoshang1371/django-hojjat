# Generated by Django 4.1.7 on 2023-06-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_information', '0016_alter_postaddress_mobile_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postaddressdetail',
            name='carrierDetails',
            field=models.CharField(choices=[('1', 'post'), ('2', 'tipox'), ('3', 'freight')], default='post', max_length=20, verbose_name='روش ارسال'),
        ),
    ]