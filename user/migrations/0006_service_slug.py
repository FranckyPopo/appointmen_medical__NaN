# Generated by Django 4.0.5 on 2022-08-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_service_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
