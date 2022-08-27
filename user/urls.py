from django.urls import path

from user import views

urlpatterns = [
    path("dashbord/add-service/", views.UserAddService.as_view(), name="user_add_service"),   
    path("dashbord/list-services/", views.UserListService.as_view(), name="user_list_services"),   
    path('dashbord/appointment/', views.UserAppoitment.as_view(), name="user_appointment"),
    path('appointment/detail/<int:pk_appointmen>/', views.UserAppoitmentDetail.as_view(), name="user_appointment_detail"),
    path('appointment/delete/<int:pk_appointment>/', views.UserAppoitmentDelete.as_view(), name="appointment_delete"),
    path(
        "list-service/delete-service/<int:pk_service>/", 
        views.UserDeleteService.as_view(), 
        name="user_delete_service"
    ),   
    path(
        "list-service/edit-service/<int:pk_service>/", 
        views.UserEditService.as_view(), 
        name="user_edit_service"
    ), 
    path('health-centers/<slug:slug_town>/', views.UserHealthCenters.as_view(), name="user_health_centers"),
    path('health-center/<slug:slug_user>/', views.UserHealthCenterDetail.as_view(), name="user_health_center_detail"),
]







































