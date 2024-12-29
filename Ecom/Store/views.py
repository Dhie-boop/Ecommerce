from django.shortcuts import render
from .models import *

# My views are here

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)



def cart(request):
    context = {}
    return render(request, 'Store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'Store/checkout.html', context)
