from django.shortcuts import render

from pages.models import Teams
from cars.models import Car

# Create your views here.

# create a sample function
def home(request):
    team = Teams.objects.all()
    featured_car = Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_car = Car.objects.order_by('-created_date')[:6]

    # to dislay team members in home and about page 
    empl = {
        'teams' : team,
        'featured_cars': featured_car,
        'latest_car': latest_car 
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