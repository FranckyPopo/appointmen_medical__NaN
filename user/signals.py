from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.urls import reverse
from django.utils.text import slugify

import uuid

from authentication.models import AccountVerification, Town
from user.models import Service, Appointmen

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
        
@receiver(post_save, sender=Appointmen)
def confirmation_appointmen(instance, created, **kwargs):      
    if created:
        email_center = instance.email
        url = reverse("front_contact")
        body = f"""
        Félicitation vôtre rendez-vous a été pris avec success pour le {instance.date_appointmen}.
        Veuillez vous presenter à la date indiqué au rendez-vous. 
        En cas de non présence le rendez-vous sera annulé automatiquement.
        Pour toutes question veuillez nous contacter: http://127.0.0.1:8000{url}
        """
        # Envoie email    
        email = EmailMessage('Bienvenue sur Health access', body, to=[email_center])
        email.send()

@receiver(pre_save, sender=get_user_model())
@receiver(pre_save, sender=Town)
@receiver(pre_save, sender=Service)
def generator_slug(instance, **kwargs):
    if isinstance(instance, get_user_model()):
        instance.slug = f"{slugify(instance.medical_center_name)}-abidjan-cote-ivoire"
        return 
    
    if instance.slug:
        instance.slug = slugify(instance.name)
        
