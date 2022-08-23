from django.urls import path

from front import views

urlpatterns = [
    path('', views.FrontIndex.as_view(), name="front_index"),
    path('contact/', views.FrontContact.as_view(), name="front_contact"),
    
]
