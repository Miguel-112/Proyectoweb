# Generated by Django 4.0.6 on 2022-08-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='imagen',
            field=models.ImageField(upload_to='servicios'),
        ),
    ]
