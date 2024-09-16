from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_profile, name="user-profile"),
    path('user/<id>/', views.update_user_profile, name="update-user-profile"),
]