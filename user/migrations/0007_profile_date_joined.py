# Generated by Django 3.0.5 on 2020-05-10 10:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_profile_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
    ]
