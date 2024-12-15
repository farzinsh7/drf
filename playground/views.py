from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Order, OrderItem

# Create your views here.


def say_hello(request):

    products = Product.objects.prefetch_related('promotions').all()

    return render(request, 'hello.html', {'name': 'Farzin', 'products': list(products)})
