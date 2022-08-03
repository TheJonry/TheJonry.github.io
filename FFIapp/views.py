from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def products(request):
    return render(request, 'productMenu.html', {})

def vendors(request):
    return render(request, 'vendorMenu.html', {})