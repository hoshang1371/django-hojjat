# Generated by Django 4.1.7 on 2023-07-04 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_information', '0026_paymentmethodedetail_termsandrules_field_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paymentmethodedetail',
            options={'verbose_name': 'پذیرفتن شرایط', 'verbose_name_plural': 'پذیرفتن شرایط'},
        ),
        migrations.RemoveField(
            model_name='paymentmethodedetail',
            name='TermsAndRules_field',
        ),
    ]
