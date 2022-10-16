# Generated by Django 4.1.1 on 2022-10-06 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_hh_app', '0004_alter_resume_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='user',
        ),
        migrations.CreateModel(
            name='UsersID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
