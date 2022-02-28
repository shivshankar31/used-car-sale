from django.shortcuts import render

# Create your views here.

# create a sample function
def home(request):
    return render(request, 'pages/home.html')