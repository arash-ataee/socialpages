# Generated by Django 3.0.5 on 2020-05-06 16:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='edit_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
