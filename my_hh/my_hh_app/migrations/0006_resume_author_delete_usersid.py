# Generated by Django 4.1.1 on 2022-10-06 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_hh_app', '0005_remove_resume_user_usersid'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='author',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UsersID',
        ),
    ]
