from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
from store.models import Product, Order, OrderItem

# Create your views here.


def say_hello(request):

    products = Product.objects.filter(
        id__in=OrderItem.objects.values('product__id').distinct())

    return render(request, 'hello.html', {'name': 'Farzin', 'products': products})
