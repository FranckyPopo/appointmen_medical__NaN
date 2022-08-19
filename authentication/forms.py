from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from phonenumber_field.modelfields import PhoneNumberField


class AuthenticationFormRegister(UserCreationForm, forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            "medical_center_name",
            "email", 
            "phone_number", 
            "address", 
            "password1", 
            "password2", 
        ]
        
    email = forms.EmailField(required=True)    

class AuthenticationFormLogin(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())







