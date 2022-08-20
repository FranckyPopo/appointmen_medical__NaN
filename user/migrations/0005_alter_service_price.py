# Generated by Django 4.1 on 2022-08-20 09:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_service_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1, 'entrer un valeur supérieur à 0')]),
        ),
    ]
