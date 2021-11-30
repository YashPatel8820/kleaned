from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from HOME.views import *


urlpatterns = [
    
    path('home/', home_page, name='Home'),
    path('services/', service_page, name='Service'),
    path('bathroom/<int:pk>/', bath_page, name='Bathroom'),
]