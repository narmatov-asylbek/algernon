# Generated by Django 3.2.3 on 2021-06-09 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_view_counts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='view_counts',
            new_name='views',
        ),
    ]