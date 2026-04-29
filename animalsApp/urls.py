from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='animals-home'),
path('about/', views.about, name='animals-about'),
path('species/', views.species, name='plants-species'),
path('locations/', views.locations, name='plants-locations'),
path('medicinal/', views.species, name='medicinal-plants'),
path('contact/', views.contact, name='contact-us')
]