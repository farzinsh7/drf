from django.shortcuts import render
from store.models import Product, Order, OrderItem, Customer, Collection

# Create your views here.


def say_hello(request):
    collection = Collection()
    collection.title = 'Video Games'
    collection.featured_product = Product(
        pk=1)  # or you can use only id like 1
    collection.save()

    return render(request, 'hello.html', {'name': 'Farzin'})
