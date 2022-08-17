from django.contrib import admin
from authentication import models

@admin.register(models.Country)
class Country(admin.ModelAdmin):
    list_diplay = "__all__"    

@admin.register(models.City)
class City(admin.ModelAdmin):
    list_diplay = "__all__"
    
@admin.register(models.Town)
class Town(admin.ModelAdmin):
    list_diplay = "__all__"
    
@admin.register(models.User)
class User(admin.ModelAdmin):
    list_diplay = [
        "medical_center_name",
        "address",
        "phone_number",
        "country",
        "city",
        "town",
        "created",
        "updated",
    ]
    
@admin.register(models.AccountVerification)
class AccountVerification(admin.ModelAdmin):
    list_diplay = [
        "user", 
        "created",
        "updated",]

