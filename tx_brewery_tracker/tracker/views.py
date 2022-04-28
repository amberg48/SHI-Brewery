from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

def tracker(request):
    return render(request, 'tracker.html')
