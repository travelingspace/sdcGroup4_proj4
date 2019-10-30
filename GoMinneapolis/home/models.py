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
        
