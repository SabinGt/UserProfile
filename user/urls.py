from django.urls import path
from . import views

urlpatterns = [
    path('fillForm/',views.fillForm, name="fillForm"),
   
    path('profile/',views.my_profile, name="profile"),

    
]
    