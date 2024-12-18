from django.urls import path
from . import views

app_name = "store"
# URLConf
urlpatterns = [
    path('products/', views.ProductList.as_view(), name="product_list"),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name="product_detail"),
    path('collection/', views.CollectionList.as_view(), name="collection_list"),
    path('collection/<int:pk>/', views.CollectionDetail.as_view(),
         name="collection_detail"),
]
