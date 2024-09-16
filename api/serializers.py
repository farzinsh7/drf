from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.UserProfile
        fields = "__all__"
        

class CreateUserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.UserProfile
        fields = ["name", "age", "email", "bio"]