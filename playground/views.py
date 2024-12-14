from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Order, OrderItem

# Create your views here.


def say_hello(request):

    orders = OrderItem.objects.filter(product__collection__id=3)

    return render(request, 'hello.html', {'name': 'Farzin', 'products': list(orders)})
