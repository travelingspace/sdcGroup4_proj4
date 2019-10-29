from django.shortcuts import render
<<<<<<< HEAD
from .models import LiquorSales
=======
from .models import FireReport
from .models import neighborhood_cirme
>>>>>>> 0c12a98ceb1732ffac3dc285724d9ced54ce6cc6

# Create your views here.

def home(request):
<<<<<<< HEAD
    lsales = LiquorSales.getBusinesses()
    return render(request, 'home.html', { 'liquorStos': lsales})
=======
    incidents = FireReport.objects.all()
    '''incident = FireReport.GetIncident()'''
    return render(request, 'home.html', { 'fire_incidents': incidents})

def neighborhood(request):
    neighborhoods = neighborhood_crime.objects.all()
    crimes = crimeReport.
>>>>>>> 0c12a98ceb1732ffac3dc285724d9ced54ce6cc6
