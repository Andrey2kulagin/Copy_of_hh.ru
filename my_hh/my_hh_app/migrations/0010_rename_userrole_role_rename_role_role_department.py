# Generated by Django 4.1.1 on 2022-10-08 07:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_hh_app', '0009_userrole'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserRole',
            new_name='Role',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='Role',
            new_name='department',
        ),
    ]
