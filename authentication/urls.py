from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from authentication import views

urlpatterns = [
    path("register/", views.AuthenticationRegister.as_view(), name="authentication_register"),
    path("login/", views.AuthenticationLogin.as_view(), name="authentication_login"),
    path("dashbord/logout/", views.AuthenticationLogout.as_view(), name="authentication_logout"),
    path(
        "verification-account/<uuid:token>/", 
        views.AuthenticationVerificationAccount.as_view(), 
        name="authentication_verification_account"
    ),    
    path(
        "dashbord/edit-profile/", 
        views.AuthenticationEditProfile.as_view(), 
        name="authentication_edit_profile"
    ),
    path(
        "dashbord/change-password/", 
        views.AuthenticationPasswordChange.as_view(), 
        name="authentication_change_passwor"
    ),
    path(
        "change-password/done/", 
        views.AuthenticationPasswordResetDone.as_view(), 
        name="authentication_change_passwor_done"
    ),
    
    
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )