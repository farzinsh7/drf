from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Order, OrderItem

# Create your views here.


def say_hello(request):

    queryset = OrderItem.objects.select_related(
        'product', 'order__customer').order_by('-order__placed_at')[:5]

    return render(request, 'hello.html', {'name': 'Farzin', 'queryset': list(queryset)})
