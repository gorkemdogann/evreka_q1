# Generated by Django 3.1.7 on 2021-03-11 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evraka', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigationrecord',
            name='date',
            field=models.DateTimeField(verbose_name='Oluşturulma Tarihi'),
        ),
    ]
