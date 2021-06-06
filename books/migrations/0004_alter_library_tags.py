# Generated by Django 3.2.3 on 2021-06-06 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_library'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='tags',
            field=models.CharField(choices=[('R', 'Читаю'), ('AR', 'Прочитано'), ('TR', 'Прочту позже'), ('Q', 'Брошено')], default='R', max_length=3),
        ),
    ]