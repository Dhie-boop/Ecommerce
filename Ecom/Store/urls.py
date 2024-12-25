from django.urls import path
from . import views

urlpatterns = [
    #the path is empty because we want the store page to be the homepage
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
]
