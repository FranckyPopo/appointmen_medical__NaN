from django.db.models.signals import pre_save 
from django.dispatch import receiver
from django.contrib.auth import get_user_model


@receiver(pre_save, sender=get_user_model())
def my_callback(instance, **kwargs):
    instance.is_active = False


