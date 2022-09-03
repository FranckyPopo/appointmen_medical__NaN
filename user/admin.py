from django.contrib import admin

from user import models


@admin.register(models.Service)
class Service(admin.ModelAdmin):
    list_display = ["name", "description", "created", "updated"]
    
@admin.register(models.Appointmen)
class Appointmen(admin.ModelAdmin):
    list_display = ["user", "name", "email"]

@admin.register(models.Contact)
class Contact(admin.ModelAdmin):
    list_display = ["message", "name", "email", "phone_number"]

