from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path('update_user_profile/',views.UpdateProfileView.as_view({'post':'update','get':'list'}),name='update-user-profile'),
]