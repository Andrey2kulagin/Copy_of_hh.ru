# Generated by Django 4.1.1 on 2022-10-16 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_hh_app', '0043_profile_alter_companies_foundation_data_result_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='foundation_data',
            field=models.DateField(default=datetime.datetime(2022, 10, 16, 16, 52, 39, 409132), null=True, verbose_name='foundation_data'),
        ),
    ]
