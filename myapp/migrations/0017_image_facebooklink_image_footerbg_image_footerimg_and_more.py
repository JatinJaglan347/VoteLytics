# Generated by Django 4.2 on 2023-05-20 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_image_backgroundimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='facebooklink',
            field=models.CharField(default=datetime.datetime(2023, 5, 20, 18, 23, 59, 473759, tzinfo=datetime.timezone.utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='footerbg',
            field=models.ImageField(default=datetime.datetime(2023, 5, 20, 18, 24, 6, 54656, tzinfo=datetime.timezone.utc), upload_to='footerimg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='footerimg',
            field=models.ImageField(default=datetime.datetime(2023, 5, 20, 18, 24, 11, 162262, tzinfo=datetime.timezone.utc), upload_to='footerimg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='instagramlink',
            field=models.CharField(default=datetime.datetime(2023, 5, 20, 18, 24, 16, 579392, tzinfo=datetime.timezone.utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='twitterlink',
            field=models.CharField(default=datetime.datetime(2023, 5, 20, 18, 24, 24, 490870, tzinfo=datetime.timezone.utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='youtubelink',
            field=models.CharField(default=datetime.datetime(2023, 5, 20, 18, 24, 28, 399718, tzinfo=datetime.timezone.utc), max_length=200),
            preserve_default=False,
        ),
    ]
