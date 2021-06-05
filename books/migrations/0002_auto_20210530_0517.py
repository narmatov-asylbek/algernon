# Generated by Django 3.2.3 on 2021-05-30 05:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookInfo',
            new_name='Book',
        ),
        migrations.RenameModel(
            old_name='BookCycle',
            new_name='Cycle',
        ),
        migrations.RenameModel(
            old_name='BookGenre',
            new_name='Genre',
        ),
        migrations.RenameModel(
            old_name='BookType',
            new_name='Type',
        ),
    ]
