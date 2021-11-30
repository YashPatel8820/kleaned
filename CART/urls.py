from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *


urlpatterns = [
    path('h/', hii),
    path('cart/', cart_page, name="Cart"),
    path('checkout/', checkout_page, name="Checkout"),
    path('add/<int:pk>/', addcart_page, name="Add"),
    path('remove/<int:pk>/', remove_cart, name="Remove"),
    path('place/', place_order, name="Place"),

]

