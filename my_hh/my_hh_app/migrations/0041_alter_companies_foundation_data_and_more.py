# Generated by Django 4.1.1 on 2022-10-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_hh_app', '0040_alter_skills_is_checked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='foundation_data',
            field=models.DateField(null=True, verbose_name='foundation_data'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='industry',
            field=models.CharField(max_length=200, null=True, verbose_name='industry'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='strategy_description',
            field=models.TextField(null=True, verbose_name='Strategy_description'),
        ),
    ]
