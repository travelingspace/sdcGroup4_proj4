from django.shortcuts import render
from .models import LiquorSales

# Create your views here.

def home(request):
    return render(request, 'home.html')

def main(request):
    ls = LiquorSales()
    lsales = ls.getBusinesses()
    return render(request, 'main.html', { 'liquorStos': lsales})
