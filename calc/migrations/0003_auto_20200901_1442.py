# Generated by Django 3.0.7 on 2020-09-01 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_auto_20200827_0722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default='SOME STRING', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]