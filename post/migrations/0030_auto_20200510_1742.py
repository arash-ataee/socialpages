# Generated by Django 3.0.5 on 2020-05-10 17:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0029_auto_20200510_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
    ]
