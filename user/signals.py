from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage

import uuid

from authentication.models import AccountVerification


@receiver(post_save, sender=get_user_model())
def sending_registration_confirmation_email(instance, **kwargs):
    account = AccountVerification.objects.create(user=instance)
    token = account.token
    email_centre = account.user.email
    url = None
    body = f"""
    Félicitation vous venez de crée vôtre compte.
    Cliquer sur le lien pour l'activer: {url}
    """
    # Envoie email    
    email = EmailMessage('Création du compte', body, to=[email_centre])
    email.send()


