from django import forms
from django.contrib.auth import get_user_model

from user.models import Service, Appointmen

class FormService(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name", "description", "photo"]
        
class UserFormAppoitmen(forms.ModelForm):
    email = forms.EmailField(required=True)
    date_appointmen = forms.DateField(required=True)
    
    class Meta:
        model = Appointmen
        fields = ["name", "phone_number", "message", "motif", "email", "date_appointmen"]
        

