# Generated by Django 3.0 on 2020-01-23 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vdrive', '0014_video_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.URLField(max_length=250, verbose_name='thumbnail of the video'),
        ),
    ]