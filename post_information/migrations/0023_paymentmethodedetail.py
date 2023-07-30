# Generated by Django 4.1.7 on 2023-07-03 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_information', '0022_postaddress_iscorrect_mobile_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethodeDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PaymentDetails', models.CharField(choices=[('1', 'زرین پال')], default=1, max_length=20, verbose_name='روش ارسال')),
            ],
        ),
    ]
