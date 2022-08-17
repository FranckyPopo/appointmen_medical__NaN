from django.urls import path

from authentication.views import AuthenticationRegister

urlpatterns = [
    path("register/", AuthenticationRegister.as_view(), name="authentication_register"),
]