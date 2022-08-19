from django.contrib import admin

from user import models


@admin.register(models.Service)
class Service(admin.ModelAdmin):
    list_display = ["name", "price", "description", "created", "updated"]
    
@admin.register(models.Appointmen)
class Appointmen(admin.ModelAdmin):
    exclude = ["message"]

