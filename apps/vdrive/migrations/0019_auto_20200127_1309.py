# Generated by Django 3.0 on 2020-01-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vdrive', '0018_auto_20200127_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='size',
            field=models.IntegerField(verbose_name='File size'),
        ),
    ]
