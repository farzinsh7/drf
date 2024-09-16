from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models


@api_view(['GET', 'POST'])
def user_profile(request):
    
    if request.method == "GET":
        data = models.UserProfile.objects.all()
        serializer_data = serializers.UserProfileSerializer(data, many=True)
        
        return Response(serializer_data.data)  
    
    if request.method == "POST":
        
        req_data = request.data
        
        serializer = serializers.CreateUserProfileSerializer(data=req_data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201) 
    


@api_view(['PUT', 'DELETE'])
def update_and_delete_user_profile(request, id):
    
    try:
        user_profile_obj = models.UserProfile.objects.get(id=id)
    except models.UserProfile.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


    if request.method == "PUT":
        
        serializer = serializers.UserProfileSerializer(
        instance=user_profile_obj,
        data=request.data, 
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "DELETE":
        
        user_profile_obj.delete()
        return Response({'message': 'UserProfile deleted successfully'}, status=status.HTTP_204_NO_CONTENT)