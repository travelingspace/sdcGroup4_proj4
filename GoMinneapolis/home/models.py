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

        self.liquor_licenses = []

        for sto in data["features"]:
            
            name = sto["attributes"]["licenseName"]
            address = sto["attributes"]["address"]
            saleType = sto["attributes"]["liquorType"]

            new_entry = {name, address, saleType}
            self.liquor_licenses.append(new_entry) 
                       
        return self.liquor_licenses
        
