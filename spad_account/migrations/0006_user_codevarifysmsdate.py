# Generated by Django 4.1.7 on 2023-10-28 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spad_account', '0005_remove_user_email2'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='codeVarifySmsDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='زمان تایید پیامکی'),
        ),
    ]
