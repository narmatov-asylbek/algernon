# Generated by Django 3.2.3 on 2021-05-30 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20210530_1115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'ordering': ['-created_at'], 'verbose_name': 'Chapter', 'verbose_name_plural': 'Chapters'},
        ),
    ]
