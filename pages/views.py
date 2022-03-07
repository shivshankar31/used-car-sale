from django.shortcuts import render

from pages.models import Teams

# Create your views here.

# create a sample function
def home(request):
    team = Teams.objects.all()

    # to dislay team members in home and about page 
    empl = {
        'teams' : team
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