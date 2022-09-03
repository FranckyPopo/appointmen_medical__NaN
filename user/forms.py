from django import forms

from user.models import Service, Appointmen, Contact

class FormService(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name", "description", "photo"]
        
class UserFormAppoitmen(forms.ModelForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = Appointmen
        fields = [
            "name", 
            "phone_number", 
            "message", 
            "motif", 
            "email",
            "date_appointmen"
        ]
        
class UserContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "name",
            "email",
            "phone_number",
            "message",
        ]


