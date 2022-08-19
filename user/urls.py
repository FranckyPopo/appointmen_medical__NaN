from django.urls import path

from user.views import UserDashbord

urlpatterns = [
    path("dashbord/", UserDashbord.as_view(), name="user_dashbord"),    

    
]







































