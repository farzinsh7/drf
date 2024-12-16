from django.shortcuts import render
from store.models import Product, Order, OrderItem, Customer, Collection

# Create your views here.


def say_hello(request):
    # collection = Collection(pk=11)
    # collection.title = 'Games'
    # collection.featured_product = None
    # collection.save()

    # or the better way
    Collection.objects.filter(pk=11).update(title='Video Games')

    return render(request, 'hello.html', {'name': 'Farzin'})
