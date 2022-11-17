# Generated by Django 4.1.1 on 2022-10-18 15:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_hh_app', '0055_alter_companies_foundation_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='foundation_data',
            field=models.DateField(default=datetime.datetime(2022, 10, 18, 15, 56, 23, 404756), null=True, verbose_name='foundation_data'),
        ),
        migrations.AlterField(
            model_name='usercheckedskills',
            name='skills_id',
            field=models.ManyToManyField(default='Подтвержденных навыков нет', to='my_hh_app.skills'),
        ),
        migrations.AlterField(
            model_name='usercheckedskills',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
