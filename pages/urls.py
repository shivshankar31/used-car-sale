# step 2: create urls.py and import views  

from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.home, name='home'),
]
