from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F, Value, ExpressionWrapper, Max, Count, Sum
from store.models import Product, Order, OrderItem, Customer, Collection

# Create your views here.


def say_hello(request):
    result = Product.objects.annotate(best_seller=Sum(F(
        'orderitem__unit_price') * F('orderitem__quantity'))).order_by('-best_seller')[:5]

    return render(request, 'hello.html', {'name': 'Farzin', 'result': result})
