# Generated by Django 4.1.1 on 2022-10-08 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_hh_app', '0010_rename_userrole_role_rename_role_role_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='department',
            new_name='role',
        ),
    ]
