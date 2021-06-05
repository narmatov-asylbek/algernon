# Generated by Django 3.2.3 on 2021-05-30 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_cycle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('F', 'Finished'), ('В', 'Draft'), ('N', 'Not finished')], default='N', max_length=2),
        ),
    ]
