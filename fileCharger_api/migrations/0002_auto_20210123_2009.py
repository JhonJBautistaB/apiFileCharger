# Generated by Django 3.1.5 on 2021-01-24 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileCharger_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='file_name',
            field=models.FileField(upload_to='./files/'),
        ),
    ]