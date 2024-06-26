# Generated by Django 4.0.3 on 2024-05-22 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0007_alter_movie_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('two', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('three', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('four', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('five', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='movie.movie')),
            ],
            options={
                'ordering': [],
            },
        ),
    ]
