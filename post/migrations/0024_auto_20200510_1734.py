# Generated by Django 3.0.5 on 2020-05-10 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0023_post_edit_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-edit_date',)},
        ),
        migrations.RemoveField(
            model_name='post',
            name='date_of_create',
        ),
    ]
