from django.db import models
import requests

# Create your models here.
            
class LiquorSales(models.Model):

    licenseName = models.CharField(max_length=200)
    liquorType = models.CharField(max_length=100)
    address = models.CharField(max_length=300)

    def _str_(self):
        
        return f'{self.licenseName} has a license for {self.liquorType} at address: {self.address}'
    
    def getBusinesses(self):
        
        data = requests.get('https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/Off_Sale_Liquor/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json').json()

        self.liquor_licenses = {}
        cntr = 0

        for sto in data["features"]:
            
            name = sto["attributes"]["licenseName"]
            address = sto["attributes"]["address"]
            saleType = sto["attributes"]["liquorType"]
            lat = sto["attributes"]["lat"]
            lng = sto["attributes"]["long"]
            
            new_entry = {name : {"address": address, "saleType": saleType, "lat":lat, "lng":lng}}
            self.liquor_licenses.update(new_entry)

            cntr += 1 
                       
        return self.liquor_licenses
    
    def lat_long_to_zip(self, lat, lng):
       query_string_url = ("https://public.opendatasoft.com/api/records/1.0/search/?dataset=us-zip-code-latitude-and-longitude&facet=state&facet=timezone&facet=dst&facet=city&refine.state=MN&refine.city=Minneapolis&refine.latitude=" + str(lat) + "&refine.longitude=" + str(lng)) 
       data = requests.get(query_string_url).json()

       zip_code = 00000       
       
       for i in data["records"]:
           zip_code = i["fields"]["zip"]           
           
       return zip_code 
        
class yelpRestaurants(models.Model):
    restaurantName = models.CharField(max_length=200)
    restaurantRating = models.IntegerField
    restaurantLocation = models.CharField(max_length=500)

    def searchYelp(self, zip_code):
        yelpList = {}
        YELP_API_KEY = 'f3n-U3oZBl9eE1_a6_PNLZjs0Phcgs0zQDdaVvuMYq8dBntIB1h5yU9b2-xqBb-FD_i3gPqWY0Mx-BkkITo-V8uQ2LQ5cTXyFAiGn57FuHeSmoMBJFDJ3HwGRumoXXYx'

        yelp_url = 'https://api.yelp.com/v3/businesses/search'

        headers = {'Authorization': 'Bearer ' + YELP_API_KEY}

        params = {
            'categories': 'restaurants',
            'location': zip_code,
            'radius': '1000',
            'limit': 20,
            'sort_by': 'rating'
        }

        response = requests.get(yelp_url, headers=headers, params=params).json()

        restaurants = response['businesses']

        for r in restaurants:
            name = r['name']
            rating = r['rating']
            location = r['location']
            address = ','.join(location['display_address'])

            newEntry = {name: { "rating": rating, "address": address }}
            
            yelpList.update(newEntry)
        
        return(yelpList)

class ZipCode(models.Model):
    
    zipcode = models.CharField(max_length=20)

    