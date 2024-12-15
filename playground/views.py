from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Count, Max, Min, Avg
from store.models import Product, Order, OrderItem

# Create your views here.


def say_hello(request):

    result = Product.objects.filter(collection__id=3).aggregate(minimum_unit=Min(
        'unit_price'), maximum_unit=Max('unit_price'), average=Avg('unit_price'))

    return render(request, 'hello.html', {'name': 'Farzin', 'result': result})
