from django.shortcuts import render
from .models import LiquorSales

# Create your views here.

def home(request):
    lsales = LiquorSales.getBusinesses()
    return render(request, 'home.html', { 'liquorStos': lsales})