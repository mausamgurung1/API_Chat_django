from django.contrib import admin
from django.urls import path

from home.views import ChatAPI, about, home

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('api/', ChatAPI, name='ChatAPI')
]
