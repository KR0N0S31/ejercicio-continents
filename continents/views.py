from django.shortcuts import render
from django.views.generic import ListView

from .models import Continent

# Create your views here.

class ContinentsView(ListView):
    template_name = 'continents.html'
    model = Continent
