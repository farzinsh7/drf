from django.shortcuts import render
from store.models import Product, Order, OrderItem, Customer, Collection, Cart, CartItem

# Create your views here.


def say_hello(request):
    # start create a shopping cart
    # cart = Cart()
    # cart.save()

    # item1 = CartItem()
    # item1.cart = cart
    # item1.product_id = 1
    # item1.quantity = 3
    # item1.save()
    # end create a shopping cart

    # start update a quantity of a shopping cart
    # CartItem.objects.filter(pk=1).update(quantity=6)
    # end update a quantity of a shopping cart

    # start delete a shopping cart
    # cart = Cart(pk=1)
    # cart.delete()
    # end delete a shopping cart

    return render(request, 'hello.html', {'name': 'Farzin'})
