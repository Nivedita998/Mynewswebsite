# Generated by Django 3.0.4 on 2020-04-08 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200408_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='abouttxt',
            field=models.TextField(default=''),
        ),
    ]