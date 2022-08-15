from django.db import models

from authentication.models import RepeatFields

# Create your models here.
class SiteInfo(RepeatFields):
    link_facebook = models.URLField()
    link_instagram = models.URLField()
    link_twetter = models.URLField()