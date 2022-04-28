from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
import requests

def tracker(request):
    response = requests.get("https://api.openbrewerydb.org/breweries?by_state=texas")
    package = response.json()
    b = Brewery.objects.filter(pk=package[0]['id'])
    if b:
        print(b)
    else:
        print("Not in database")
    return render(request, 'tracker.html', {'package' : package})
