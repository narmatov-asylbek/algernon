# Generated by Django 3.2.3 on 2021-06-03 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_genre_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]