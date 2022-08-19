from django.urls import path

from user.views import UserAddService

urlpatterns = [
    path("dashbord/add-service/", UserAddService.as_view(), name="user_add_service"),   

    
]







































