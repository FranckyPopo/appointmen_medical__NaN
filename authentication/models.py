from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class RepeatFields(models.Model):
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Country(RepeatFields):
    name = models.CharField(max_length=150)
    
class City(RepeatFields):
    name = models.CharField(max_length=150)
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        related_name="city_country",
    )

class Town(RepeatFields):
    name = models.CharField(max_length=150)
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True,
        related_name="town_city",
    )

class User(AbstractUser, RepeatFields):
    medical_center_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    description = models.TextField()
    phone_number = PhoneNumberField(region="CI")
    phone_number_two = PhoneNumberField(region="CI", blank=True)
    fax = PhoneNumberField(region="CI", blank=True)
    photo = models.ImageField(blank=True, upload_to="photo_user")
    
    country = models.ForeignKey(
        Country,
        models.SET_NULL,
        null=True,
    )
    city = models.ForeignKey(
        City,
        models.SET_NULL,
        null=True,
    )
    town = models.ForeignKey(
        Town,
        models.SET_NULL,
        null=True,
    )
    
    




