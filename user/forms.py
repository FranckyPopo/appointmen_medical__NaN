from django import forms
from django.contrib.auth import get_user_model

from user.models import Service

class FormService(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name", "price", "description",]
        

        
        
        

