from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from user.models import CustomUser
from .serializers import UserProfileUpdate
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponseRedirect


class UpdateProfileView(viewsets.ModelViewSet):
    serializer_class = UserProfileUpdate
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        user = self.request.user
        current_user = self.request.user
        response = {
            'post':user,
            'current_user':self.request.user,
        }
        return CustomUser.objects.get(username = user.username)
    def create(self, request, *args, **kwargs):
        response = super(UpdateProfileView, self).create(request, *args, **kwargs)
        print("this is response",response)
        return HttpResponseRedirect(redirect_to='/')  
    def update(self,request,*args,**kwargs):
        user_obj = self.request.user
        data = request.data
        user_obj.first_name = data['first_name']
        user_obj.last_name = data['last_name']
        user_obj.address = data['address']
        user_obj.phone_number = data['phone_number']
        user_obj.gender = data['gender']
        user_obj.interest = data['interest']
        user_obj.profile_image = data['profile_image']
        user_obj.profile_completed = True
        user_obj.save()
        return HttpResponseRedirect(redirect_to='/')
    



