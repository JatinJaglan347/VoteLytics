# Generated by Django 4.2 on 2023-05-18 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_image_name_candidate1_image_name_candidate2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='discription',
        ),
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
        migrations.RemoveField(
            model_name='image',
            name='name_candidate2',
        ),
        migrations.RemoveField(
            model_name='image',
            name='name_candidate3',
        ),
        migrations.RemoveField(
            model_name='image',
            name='name_candidate4',
        ),
        migrations.RemoveField(
            model_name='image',
            name='name_candidate5',
        ),
        migrations.RemoveField(
            model_name='image',
            name='name_candidate6',
        ),
    ]
