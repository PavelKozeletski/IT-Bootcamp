# Generated by Django 4.1.2 on 2022-10-28 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0004_alter_model_submodels_avarege_maintenance_prise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_submodels',
            name='avarege_maintenance_prise',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
