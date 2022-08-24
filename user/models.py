from django.db import models
from django.conf import settings 
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField

import datetime 

from authentication.models import RepeatFields

class Service(RepeatFields):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="service_user",
    )
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True) 
    description = models.TextField(max_length=200)
    slug = models.SlugField(default="")

    def __str__(self):
        return self.name
    
    @classmethod
    def get_services(cls) -> list:
        """Retourne un liste de services sans doublons"""
        qs = cls.objects.filter(active=True, user__is_active=True)
        services = []
        
        for item in qs:
            for service in services:
                if item.name == service.name:
                    break
            else:
                services.append(item)
        return services
             
class Appointmen(RepeatFields):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="appointmen_user",
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        related_name="appointmen_service",
    )
    name = models.CharField(max_length=150)
    phone_number = PhoneNumberField(region="CI")
    email = models.EmailField(blank=True)
    message = models.TextField()
    date_appointmen = models.DateField(default=datetime.date.today)
