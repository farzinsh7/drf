from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet, basename='collections')
router.register('carts', views.CartViewSet, basename='carts')

product_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
product_router.register('reviews', views.ReviewViewSet,
                        basename='product-reviews')


carts_router = routers.NestedDefaultRouter(
    router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet,
                      basename='cart-items')

# app_name = "store"
# URLConf
urlpatterns = router.urls + product_router.urls + carts_router.urls
