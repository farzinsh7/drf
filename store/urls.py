from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

app_name = "store"
# URLConf
urlpatterns = router.urls
