# Generated by Django 3.0.5 on 2020-05-10 10:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200506_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_joined',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
    ]
