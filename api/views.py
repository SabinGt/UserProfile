from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from user.models import CustomUser
from .serializers import UserProfileUpdate
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


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
        return CustomUser.objects.filter(username = user.username)
    def create(self, request, *args, **kwargs):
        response = super(UpdateProfileView, self).create(request, *args, **kwargs)
        print("this is response",response)
        return HttpResponseRedirect(redirect_to='/')  
    
    def update(self,request,*args,**kwargs):
        
        user_obj = self.request.user
        print("user obj",user_obj)
        data = request.data
        print("unformatted data",data)
        # user_obj.first_name = data['first_name']
        # user_obj.last_name = data['last_name']
        # user_obj.addresss = data['address']
        # user_obj.phone_number = data['phone_number']
        # user_obj.gender = data['gender']
        # user_obj.interest = data['interest']
        # user_obj.profile_image = data['profile_image']
        # user_obj.profile_completed = True
        # user_obj.save()
        serializer = UserProfileUpdate(instance = user_obj,data=request.data,partial = True)
        if data['profile_image'] == '':
            print("no image coming")
            if user_obj.profile_image:
                photo = user_obj.profile_image
                print("existing photo",photo)
            else:
                DEFAULT = 'user_photos/nouser.jpg'
                photo = DEFAULT
                print("no image found so setting default",photo)

        else:
            photo = data['profile_image']
            print("naya aako photo",photo)
        if serializer.is_valid():
            serializer.save(profile_completed = True,profile_image = photo)
        else:
            print("invalid data")
            print(serializer.errors)
        # return HttpResponseRedirect(redirect_to='user/profile')
        return redirect('profile')
    



