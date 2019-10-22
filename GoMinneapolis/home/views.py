from django.shortcuts import render
from .models import FireReport

# Create your views here.

def home(request):
    incidents = FireReport.objects.all()
    return render(request, 'home.html', { 'fire_incidents': incidents})