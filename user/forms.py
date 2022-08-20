from django import forms

from user.models import Service


class FormService(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name", "price", "description",]
        
        
        
        

