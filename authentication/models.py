from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

import uuid

class RepeatFields(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Country(RepeatFields):
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class City(RepeatFields):
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        related_name="city_country",
    )

    def __str__(self):
        return self.name

class Town(RepeatFields):
    name = models.CharField(max_length=150) 
    active = models.BooleanField(default=True)
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True,
        related_name="town_city",
    )
    slug = models.SlugField(blank=True)
    
    def __str__(self):
        return self.name
        
class User(AbstractUser, RepeatFields):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "phone_number"]
    email = models.EmailField(unique=True)
    medical_center_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    phone_number = PhoneNumberField(region="CI", unique=True)
    phone_number_two = PhoneNumberField(region="CI", blank=True)
    fax = PhoneNumberField(region="CI", blank=True)
    photo = models.ImageField(blank=True, upload_to="photo_user")
    is_verification_account = models.BooleanField(default=False)
    town = models.ForeignKey(
        Town,
        models.SET_NULL,
        null=True,
    )
    
    def fields_valid(self):
        if(self.email and self.medical_center_name and
           self.address and self.description and self.phone_number and self.photo):
            return True
        return False
    
    def __str__(self):
        return self.medical_center_name
        
class AccountVerification(RepeatFields):
    user = models.OneToOneField(
        User, 
        on_delete=models.SET_NULL, 
        null=True,
    )
    
    token = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.user


   
            
            
            
            
            
            
            
            
            
            
            
            
