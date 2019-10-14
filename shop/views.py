from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'shop/home-page.html')


def about(request):
    return render(request, 'shop/about.html', {'title': 'About'})


def checkout(request):
    return render(request, 'shop/checkout-page.html')
