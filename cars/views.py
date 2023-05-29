from django.shortcuts import render
# from .models import Team
# Create your views here.
def cars(request):
    return render(request, 'cars/cars.html')
