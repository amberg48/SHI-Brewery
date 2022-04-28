from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
import requests

def update(request):
    response = requests.get("https://api.openbrewerydb.org/breweries?by_state=texas")
    package = response.json()
    for brewery in package:
        b = Brewery.objects.filter(pk=brewery['id'])
        if b: # If object already in database, update it
            print("Item exists in database")
        else: # Otherwise create new brewery object for it
            b = Brewery(id=brewery['id'], name=brewery['name'], type=brewery['brewery_type'],
                street=brewery['street'], address_2=brewery['address_2'], address_3=brewery['address_3'],
                city=brewery['city'], state=brewery['state'], county_province=brewery['county_province'],
                postal_code=brewery['postal_code'], country=brewery['country'], longitude=brewery['longitude'],
                latitude=brewery['latitude'], phone=brewery['phone'], website_url=brewery['website_url'],
                updated_at=brewery['updated_at'], created_at=brewery['created_at'])
            b.save()
    return render(request, 'tracker.html', {'package' : package})

def tracker(request):
    package = Brewery.objects.all
    return render(request, 'tracker.html', {'package' : package})
