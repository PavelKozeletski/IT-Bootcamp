# Generated by Django 4.1.2 on 2022-10-29 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0009_alter_model_submodels_fuel_system_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_submodels',
            name='fuel_cost_without_taxes',
            field=models.DecimalField(decimal_places=2, max_digits=3),
            preserve_default=False,
        ),
    ]
