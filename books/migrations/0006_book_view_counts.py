# Generated by Django 3.2.3 on 2021-06-09 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='view_counts',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
