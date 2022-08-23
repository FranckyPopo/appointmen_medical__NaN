from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.urls import reverse
from django.utils.text import slugify

import uuid

from authentication.models import AccountVerification, Town
from user.models import Service

@receiver(post_save, sender=get_user_model())
def sending_registration_confirmation_email(instance, created, **kwargs):
    if created:
        account = AccountVerification.objects.create(user=instance)
        token = account.token
        email_centre = account.user.email
        url = reverse(
            "authentication_verification_account",
            kwargs={"token": token},
        )
        body = f"""
        Félicitation vous venez de crée vôtre compte.
        Cliquer sur le lien pour l'activer: http://127.0.0.1:8000{url}
        """
        # Envoie email    
        email = EmailMessage('Bienvenue sur Health access', body, to=[email_centre])
        email.send()


@receiver(pre_save, sender=Town)
@receiver(pre_save, sender=Service)
def generator_slug(instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
    
    
