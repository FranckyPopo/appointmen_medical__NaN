from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

# Moteur d'authentification  
class MyBackend(BaseBackend):
    USERS = get_user_model()
    
    def authenticate(self, request=None, email=None, password=None):
        try:
            user = MyBackend.USERS.objects.get(
                email=email, 
                is_verification_account=True,
                is_active=True,
            )
            if user.check_password(password):  
                return user
            return None
        except:
            return None
         
    def get_user(self, user_id):
        try:
            return MyBackend.USERS.objects.get(pk=user_id)
        except:
            return None
            
         