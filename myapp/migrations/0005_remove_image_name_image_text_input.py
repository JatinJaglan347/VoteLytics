# Generated by Django 4.2 on 2023-05-17 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
        migrations.AddField(
            model_name='image',
            name='text_input',
            field=models.CharField(default=datetime.datetime(2023, 5, 17, 18, 35, 18, 736080, tzinfo=datetime.timezone.utc), max_length=100),
            preserve_default=False,
        ),
    ]
