from rest_framework import serializers 
from user.models import CustomUser
from phonenumber_field.serializerfields import PhoneNumberField

class UserProfileUpdate(serializers.ModelSerializer):
    options = (
            ('IT and Networks','IT and Networks'),
            ('UI/UX','UI/UX'),
            ('Web Development','Web Development'),
            ('Devops','Devops'),
        )
    GENDER_CHOICES = (("Male",'Male'),("Female",'Female'),("Other",'Other'))
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required = True)
    address = serializers.CharField(max_length=100,required = True)
    phone_number = PhoneNumberField(required = True)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES,required = True)
    interest = serializers.ChoiceField(choices=options,required = True)


    class Meta:
        model = CustomUser
        fields = '__all__'