# Generated by Django 4.1.1 on 2022-10-18 12:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_hh_app', '0052_alter_companies_foundation_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='foundation_data',
            field=models.DateField(default=datetime.datetime(2022, 10, 18, 12, 3, 31, 490776), null=True, verbose_name='foundation_data'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_hh_app.skills', verbose_name='Название теста'),
        ),
    ]
