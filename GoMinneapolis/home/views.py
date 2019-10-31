from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import LiquorSales
from django.http import JsonResponse
from .models import yelpRestaurants
from .models import ZipCode

# Create your views here.

def home(request):
    return render(request, 'home.html')

def main(request, zip_code):
    ls = LiquorSales()
    lsales = ls.getBusinesses()

    yelp = yelpRestaurants()
    data = yelp.searchYelp(zip_code)

    context = { 'liquorStos': lsales, 'zip_code': zip_code, "yelpData": data }
    return render(request, 'main.html', context)

def getZipFromLatLong(request):
    
    latitude = request.GET.get('lat')
    longitude = request.GET.get('lng')
    ls = LiquorSales()
    zipcode = ls.lat_long_to_zip(latitude, longitude)
    return JsonResponse(zipcode)

def getAllZips(request):
    
    all_zips = ZipCode.objects.all()
    return render(request, 'viewZipcodes.html', {"all_zips": all_zips})

def addZip(request, zip_code):
    ZipCode(zip_code).save()
    return 
    

