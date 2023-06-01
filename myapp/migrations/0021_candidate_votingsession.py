# Generated by Django 4.2 on 2023-05-22 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_remove_vote_candidate_image_name_delete_candidate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('vote_count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='VotingSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('total_voters', models.PositiveIntegerField(default=0)),
                ('candidates', models.ManyToManyField(to='myapp.candidate')),
            ],
        ),
    ]
