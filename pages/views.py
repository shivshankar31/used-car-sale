from tkinter import FLAT
from django.shortcuts import render
from cars.views import search

from pages.models import Teams
from cars.models import Car

# Create your views here.

# create a sample function
def home(request):
    team = Teams.objects.all()
    featured_car = Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_car = Car.objects.order_by('-created_date')[:6]
    # search_car = Car.objects.values('model','city', 'year', 'body_style', 'price').distinct()
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    
    
    # to dislay team members in home and about page 
    empl = {
        'teams' : team,
        'featured_cars': featured_car,
        'latest_car': latest_car,
        # 'search_car': search_car,
        'model_search': model_search,
        'year_search': year_search,
        'city_search': city_search,
        'body_style_search': body_style_search,
        
    }

    return render(request, 'pages/home.html',empl)

def about(request):
    team = Teams.objects.all()

     # to dislay team members in home and about page
    empl = {
        'teams' : team
    }

    return render(request, 'pages/about.html', empl)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')