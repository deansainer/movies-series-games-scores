# Generated by Django 4.1.7 on 2023-03-13 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='MovieScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('release_date', models.IntegerField(max_length=4)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_app.moviegenre')),
                ('score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_app.moviescore')),
            ],
        ),
    ]
