# Generated by Django 3.0.4 on 2020-04-02 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200402_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='picurl',
            field=models.TextField(default='-'),
        ),
        migrations.AlterField(
            model_name='news',
            name='picname',
            field=models.TextField(),
        ),
    ]