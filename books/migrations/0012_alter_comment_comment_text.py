# Generated by Django 3.2.3 on 2021-06-02 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_rename_text_comment_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(max_length=500),
        ),
    ]