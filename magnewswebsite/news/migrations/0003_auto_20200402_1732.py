# Generated by Django 3.0.4 on 2020-04-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200402_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='pic',
        ),
        migrations.AddField(
            model_name='news',
            name='picname',
            field=models.TextField(default='-'),
        ),
    ]