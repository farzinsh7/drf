from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserProfileList.as_view(), name="user-profile"),
    path('user/<int:pk>/', views.UserProfileDetail.as_view(), name="update-user-profile"),
]