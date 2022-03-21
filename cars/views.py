from django.shortcuts import render, get_object_or_404
from cars.models import Car

# Create your views here.

def cars(request):

    cars = Car.objects.order_by('-created_date')

    car = {
        'car': cars,
    }

    return render (request, 'cars/cars.html', car)

def car_detail(request, id):
    # detail = Car.objects.all() #normal way without 404 error
    detail = get_object_or_404(Car,pk=id) # inbuilt function

    detail = {
        'detail' : detail,
        
    }

    return render (request, 'cars/car_detail.html', detail)