# Generated by Django 3.1.5 on 2021-01-25 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fileCharger_api', '0003_auto_20210124_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='row',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='fileCharger_api.client'),
        ),
        migrations.AlterField(
            model_name='row',
            name='dataset_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dataset', to='fileCharger_api.dataset'),
        ),
    ]
