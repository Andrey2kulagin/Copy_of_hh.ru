# Generated by Django 4.1.1 on 2022-10-10 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_hh_app', '0027_alter_companies_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='author',
            field=models.CharField(max_length=200, verbose_name='Author Name'),
        ),
    ]
