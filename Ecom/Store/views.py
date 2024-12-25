from django.shortcuts import render

# My views are here

def store(request):
    context = {}
    return render(request, 'Store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'Store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'Store/checkout.html', context)
