from django.shortcuts import render
from store.models import Product, Order, OrderItem, Customer, Collection
from tags.models import TaggedItem

# Create your views here.


def say_hello(request):
    TaggedItem.objects.get_tags_for(Product, 1)

    return render(request, 'hello.html', {'name': 'Farzin'})
