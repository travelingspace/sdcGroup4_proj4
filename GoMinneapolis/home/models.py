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

            new_entry = {name : {"address": address, "saleType": saleType}}
            self.liquor_licenses.update(new_entry)

            cntr += 1 
                       
        return self.liquor_licenses
    
    def lat_long_to_zip(self):

       data = requests.get('https://public.opendatasoft.com/api/records/1.0/search/?dataset=us-zip-code-latitude-and-longitude&facet=state&facet=timezone&facet=dst&facet=city&refine.state=MN&refine.city=Minneapolis').json()

       self.code_lu = []
       
       for codes in data["records"]:
           zip_code = codes["fields"]["zip"]
           latti = codes["fields"]["latitude"]
           longit = codes["fields"]["longitude"]

           new_entry = {zip_code, latti, longit}
           self.code_lu.append(new_entry)

       return self.code_lu 
        
