# Generated by Django 3.0.7 on 2020-09-01 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_auto_20200901_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
