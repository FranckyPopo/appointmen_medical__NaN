from django import forms
from django.contrib.auth import get_user_model

from user.models import Service

class FormService(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name", "price", "description",]
        
class FormEditUser(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            "email",
            "medical_center_name",
            "address",
            "description", 
            "phone_number",
            "phone_number_two",
            "photo",
            "fax",
            "country",
            "city",
            "town",
        ]
        
        
        

