# Generated by Django 4.0.2 on 2022-06-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_service_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='value',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=9999999999999),
        ),
    ]
