from django.urls import path
from . import views

app_name = "store"
# URLConf
urlpatterns = [
    path('products/', views.product_list, name="product_list"),
    path('products/<int:pk>/', views.product_detail, name="product_detail"),
    path('collection/', views.collection_list, name="collection_list"),
    path('collection/<int:pk>/', views.collection_detail, name="collection_detail"),
]
