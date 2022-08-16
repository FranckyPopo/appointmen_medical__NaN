# Generated by Django 4.0.5 on 2022-08-16 22:21

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='CI'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photo_user'),
        ),
    ]
