# Generated by Django 4.1.2 on 2022-11-13 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
