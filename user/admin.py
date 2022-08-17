from django.contrib import admin

from user import models


@admin.register(models.Service)
class Service(admin.ModelAdmin):
    class Meta:
        list_display = "__all__"
    
@admin.register(models.Appointmen)
class Appointmen(admin.ModelAdmin):
    exclude = ["message"]

