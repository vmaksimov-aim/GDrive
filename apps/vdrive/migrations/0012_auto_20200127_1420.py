# Generated by Django 3.0 on 2020-01-27 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vdrive', '0011_auto_20200116_1406'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='processing',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='video',
            name='size',
            field=models.CharField(default=0, max_length=50, verbose_name='File size'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='status',
            field=models.CharField(choices=[('waiting on drive', 'Waiting to upload'), ('deleted', 'Successfully deleted')], default='waiting on drive', max_length=50),
        ),
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.URLField(default='https://cdn.lifehacker.ru/wp-content/uploads/2018/01/Kak-skachat-video-s-raznyx-saJtov-bez-dopolnitelnyx-programm-10-universalnyx-servisov_1515533064-1140x570.jpg', max_length=250, verbose_name='thumbnail of the video'),
            preserve_default=False,
        ),
    ]
