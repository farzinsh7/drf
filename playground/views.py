from django.shortcuts import render
from store.models import Product

# Create your views here.
def say_hello(request):
    
    product = Product.objects.get(pk=1)
    
    return render(request, 'hello.html', {'name' : 'Farzin'})