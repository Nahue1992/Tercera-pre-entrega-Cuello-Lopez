# Generated by Django 4.2.2 on 2023-06-27 00:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_remove_accion_dividendos_remove_futuro_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='futuro',
            name='ticker',
            field=models.CharField(max_length=10, validators=[django.core.validators.MaxLengthValidator(9), django.core.validators.MinLengthValidator(9)]),
        ),
    ]