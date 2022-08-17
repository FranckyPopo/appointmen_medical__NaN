from django.urls import path

from authentication.views import AuthenticationRegister, AuthenticationVerificationAccount

urlpatterns = [
    path("register/", AuthenticationRegister.as_view(), name="authentication_register"),
    path(
        "verification-account/<uuid:token>", 
        AuthenticationVerificationAccount.as_view(), 
        name="authentication_verification_account"
    ),    

    
    
]