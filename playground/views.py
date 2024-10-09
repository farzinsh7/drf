from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Order, OrderItem

# Create your views here.
def say_hello(request):
    
    orders = Order.objects.filter(customer__id=1)
    
    order_items = OrderItem.objects.filter(order__in=orders).select_related('product')
    
    product_titles = [item.product.title for item in order_items]
    
        
    return render(request, 'hello.html', {'name' : 'Farzin', 'products': product_titles})