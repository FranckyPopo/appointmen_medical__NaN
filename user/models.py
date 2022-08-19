from django.db import models
from django.conf import settings 
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField

from authentication.models import RepeatFields

class Service(RepeatFields):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="service_user",
    )
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField(validators=[MinValueValidator(1, "entrer un valeur supérieur à 0")])
    active = models.BooleanField(default=True) 
    description = models.TextField()

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

