from django.contrib.auth.backends import BaseBackend

# Moteur d'authentification  
class MyBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = User.objects.get(email=email, is_verification_account=True)
            if user.check_password(password):                   
                return user
            return None
        except:
            return None
         
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except:
            return None
            
         