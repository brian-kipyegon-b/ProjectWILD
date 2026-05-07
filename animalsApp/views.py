from django.shortcuts import render
from .models import Animal
from plantsApp.models import Car
from plantsApp.models import Plant 

# Create your views here.
def home(request):
    animals = Animal.objects.all
    context = {"data": animals}
    return render(request, 'animalsApp/home.html', context)

def about(request):
    plants = Plant.objects.all
    context = { "data": plants}
    return render(request, 'animalsApp/about.html', context)   

def species(request):
    cars = Car.objects.all
    context = {"data": cars}
    return render(request, 'plantsApp/species.html', context)   

def locations(request):
    context = {}
    return render(request, 'plantsApp/locations.html', context)   

def tour(request):
    context = {}
    return render(request, 'plantsAppp/medicinal.html', context) 

def contact(request):
    context = {}
    return render(request, 'animalsApp/contact.html', context)      