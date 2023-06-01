# Generated by Django 4.2 on 2023-05-17 08:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_image_candidate1'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='candidate2',
            field=models.ImageField(default=datetime.datetime(2023, 5, 17, 8, 37, 55, 579352, tzinfo=datetime.timezone.utc), upload_to='candidate2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='candidate3',
            field=models.ImageField(default=datetime.datetime(2023, 5, 17, 8, 38, 3, 972267, tzinfo=datetime.timezone.utc), upload_to='candidate3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='candidate4',
            field=models.ImageField(default=datetime.datetime(2023, 5, 17, 8, 38, 8, 854307, tzinfo=datetime.timezone.utc), upload_to='candidate4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='candidate5',
            field=models.ImageField(default=datetime.datetime(2023, 5, 17, 8, 38, 12, 709988, tzinfo=datetime.timezone.utc), upload_to='candidate5'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='candidate6',
            field=models.ImageField(default=datetime.datetime(2023, 5, 17, 8, 38, 16, 101420, tzinfo=datetime.timezone.utc), upload_to='candidate6'),
            preserve_default=False,
        ),
    ]
