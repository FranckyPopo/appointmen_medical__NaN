from django.urls import path

from authentication import views

urlpatterns = [
    path("register/", views.AuthenticationRegister.as_view(), name="authentication_register"),
    path("login/", views.AuthenticationLogin.as_view(), name="authentication_login"),
    path(
        "verification-account/<uuid:token>", 
        views.AuthenticationVerificationAccount.as_view(), 
        name="authentication_verification_account"
    ),    
    
    path(
        "user/edit-profile/", 
        views.AuthenticationEditProfile.as_view(), 
        name="authentication_edit_profile"
    ),
    
    
]