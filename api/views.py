from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201) 
        else:
            return Response(serializer.errors, status=400)
            
   

