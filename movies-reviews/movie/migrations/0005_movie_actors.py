# Generated by Django 4.0.3 on 2024-05-21 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_movie_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.CharField(default=2000, max_length=250),
            preserve_default=False,
        ),
    ]
