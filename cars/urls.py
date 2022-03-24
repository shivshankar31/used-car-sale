from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.cars, name='cars'),
    path('<int:id>',views.car_detail, name='car_detail'),
    path('search', views.search, name='search'),

]