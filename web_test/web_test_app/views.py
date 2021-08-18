from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'web_test_app/home.html')

def products(request):
    return render(request, 'web_test_app/products.html')

def costumer(request):
    return render(request, 'web_test_app/costumer.html')