from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from USER.views import *

urlpatterns = [
    path('one/', hello, name="h"),
    path('login/', login_page, name="Login"),
    path('register/', register_page, name="Register"),
    path('logout/', logout_page, name="Logout"),
]
