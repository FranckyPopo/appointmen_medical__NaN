from django.urls import path

from user.views import UserRegister

urlpatterns = [
    path("register/", UserRegister.as_view(), name="user_register"),
]