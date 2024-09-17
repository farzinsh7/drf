from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from . import serializers
from . import models


class UserProfileList(APIView):
    
    
    def post(self, request):
        
        serializer = serializers.CreateUserProfileSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)        
    
    
    def get(self, request):
        
        all_user_profile_obj = models.UserProfile.objects.all()
        
        serializer = serializers.UserProfileSerializer(
            all_user_profile_obj,
            many=True
        )
        
        return Response(serializer.data)
    


class UserProfileDetail(APIView):
    
    
    def get_object(self, pk):
        try:
            return models.UserProfile.objects.get(pk=pk)
        except models.UserProfile.DoesNotExist:
            raise Http404    
    
    
    def get(self, request, pk):
        
        user_profile_obj = self.get_object(pk)
        
        serializer = serializers.UserProfileSerializer(
            user_profile_obj,
        )
        
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        
        user_profile_obj = self.get_object(pk)
        
        serializer = serializers.UserProfileSerializer(
            instance = user_profile_obj,
            data= request.data
        )
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
    def delete(self, request, pk):
        
        user_profile_obj = self.get_object(pk)
        
        user_profile_obj.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)