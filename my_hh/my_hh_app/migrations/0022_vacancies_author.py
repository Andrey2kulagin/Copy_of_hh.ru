# Generated by Django 4.1.1 on 2022-10-09 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_hh_app', '0021_vacancies_delete_vacansies_companies_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancies',
            name='author',
            field=models.CharField(max_length=200, null=True, verbose_name='User Name'),
        ),
    ]
