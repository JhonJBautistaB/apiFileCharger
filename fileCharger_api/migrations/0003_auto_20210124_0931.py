# Generated by Django 3.1.5 on 2021-01-24 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileCharger_api', '0002_auto_20210123_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='file_name',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]
