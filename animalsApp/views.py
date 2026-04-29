from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'animalsApp/home.html', context)

def about(request):
    context = {}
    return render(request, 'animalsApp/about.html', context)   

def species(request):
    context = {}
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