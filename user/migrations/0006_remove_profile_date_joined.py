# Generated by Django 3.0.5 on 2020-05-10 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200510_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_joined',
        ),
    ]
