# Generated by Django 3.0.5 on 2020-05-10 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0024_auto_20200510_1734'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-id',)},
        ),
        migrations.RemoveField(
            model_name='post',
            name='edit_date',
        ),
    ]
