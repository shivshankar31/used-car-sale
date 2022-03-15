from django.shortcuts import render
from cars.models import Car

# Create your views here.

def cars(request):

    cars = Car.objects.all()

    car = {
        'car': cars
    }

    return render (request, 'cars/cars.html', car)