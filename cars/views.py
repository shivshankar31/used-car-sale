from django.shortcuts import render, get_object_or_404
from cars.models import Car
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def cars(request):

    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 3) 
    page = request.GET.get('page')
    page_car = paginator.get_page(page)

    car = {
        'car': page_car,
    }

    return render (request, 'cars/cars.html', car)

def car_detail(request, id):
    # detail = Car.objects.all() #normal way without 404 error
    detail = get_object_or_404(Car,pk=id) # inbuilt function

    detail = {
        'detail' : detail,
        
    }

    return render (request, 'cars/car_detail.html', detail)