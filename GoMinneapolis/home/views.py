from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import LiquorSales

# Create your views here.

def home(request):
    return render(request, 'home.html')

def main(request, zip_code):
    ls = LiquorSales()
    lsales = ls.getBusinesses()
    context = { 'liquorStos': lsales, 'zip_code': zip_code }
    return render(request, 'main.html', context)