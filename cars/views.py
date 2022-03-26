from ast import keyword
from django.shortcuts import render, get_object_or_404
from cars.models import Car
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

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

def search(request):
    search_data = Car.objects.order_by('-created_date')

    

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            data = search_data.filter(Q(description__icontains = keyword)|Q(car_title__icontains=keyword))

    
        
    # if 'key' in request.GET:
    #     search_fields = ['year','city','model','body_style']
    #     for key in search_fields:
    #         keyword = request.GET[key]
    #         if keyword:
    #             data = search_data.filter(keyword__iexact=key)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            data = search_data.filter(year__iexact=year)
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            data = search_data.filter(city__iexact=city)
    
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            data = search_data.filter(model__iexact=model)
    
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            data = search_data.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            data = search_data.filter(price__gte=min_price, price__lte=max_price)



    # data1 = {
    #     'data': search_data,
    # }

    return render(request, 'cars/search.html', {'data': data,})