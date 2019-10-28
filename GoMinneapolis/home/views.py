from django.shortcuts import render
from .models import FireReport
from .models import neighborhood_cirme

# Create your views here.

def home(request):
    incidents = FireReport.objects.all()
    '''incident = FireReport.GetIncident()'''
    return render(request, 'home.html', { 'fire_incidents': incidents})

def neighborhood(request):
    neighborhoods = neighborhood_crime.objects.all()
    crimes = crimeReport.