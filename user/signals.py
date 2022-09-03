from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
import environ

import uuid

from authentication.models import AccountVerification, Town
from user.models import Service, Appointmen, Contact

env = environ.Env()
environ.Env.read_env(env_file=str(settings.BASE_DIR / "appointmen" / ".env"))
url_domaine = env('ALLOWED_HOSTS')

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
        Cliquer sur le lien pour l'activer: https://{url_domaine}{url}
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
        Félicitation vôtre rendez-vous a été pris avec success pour le {instance.date_appointmen.strftime("%d/%m/%Y")}.
        Veuillez vous presenter à la date indiqué au rendez-vous. 
        En cas de non présence le rendez-vous sera annulé automatiquement.
        Pour toutes autres questions veuillez nous contacter: https://{url_domaine}{url}
        """
        # Envoie email    
        email = EmailMessage('Rendez-vous pris avec success', body, to=[email_center])
        email.send()
     
        
@receiver(post_save, sender=Contact)
def confirmation_contact(instance, created, **kwargs): 
    if created:
        email = instance.email
        body = f"""
        Votre demande de contact fait l'objet d'un traitement.
        Nous vous rencontrerons bientôt. """
        # Envoie email    
        email = EmailMessage('Rendez-vous pris avec success', body, to=[email])
        email.send()


@receiver(pre_save, sender=get_user_model())
@receiver(pre_save, sender=Town)
@receiver(pre_save, sender=Service)
def generator_slug(instance, **kwargs):
    if isinstance(instance, get_user_model()):
        instance.slug = f"{slugify(instance.medical_center_name)}-abidjan-cote-ivoire"
        return 
    
    instance.slug = slugify(instance.name)
        
