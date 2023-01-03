# Generated by Django 4.1.1 on 2022-10-18 15:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_hh_app', '0056_alter_companies_foundation_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='foundation_data',
            field=models.DateField(default=datetime.datetime(2022, 10, 18, 15, 58, 52, 597576), null=True, verbose_name='foundation_data'),
        ),
        migrations.AlterField(
            model_name='usercheckedskills',
            name='skills_id',
            field=models.ManyToManyField(null=True, to='my_hh_app.skills'),
        ),
    ]