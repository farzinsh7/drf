from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from . import models


@api_view(['GET', 'POST'])
def user_profile(request):
    
    data = models.UserProfile.objects.all()
    serializer_data = serializers.UserProfileSerializer(data, many=True)
    
    return Response(serializer_data.data)
    

