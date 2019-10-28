from django.db import models
import requests

# Create your models here.
class FireReport(models.Model):

    ''' 
            311 API url - https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/Fires_Reported_2019_YTD/FeatureServer/0/query?where=1%3D1&outFields=inci_no,descript,alm_date,alm_time,number,street,st_type,st_suffix,addr_2,apt_room,latitude,longitude,inci_type,clr_date,clr_time,alarms,complete,StartDate,EndDate,OBJECTID&outSR=4326&f=json
    '''

    inci_no = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    alm_date = models.DateField()
    alm_time = models.TimeField()
    building_num = models.CharField(max_length=100)
    street_num = models.CharField(max_length=100)
    lattitude = models.FloatField()
    longitude = models.FloatField()
    incident_type = models.CharField(max_length=100)

    def _str_(self):
        return f'{self.inci_no}, on {self.alm_date} at {self.alm_time} was reported at location address {self.building_num}, {self.street_num}. It was of incident type {self.incident_type}.'

    '''def GetIncident():
        allIncidents = requests.get('https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/Fires_Reported_2019_YTD/FeatureServer/0/query?where=1%3D1&outFields=inci_no,descript,alm_date,alm_time,number,street,st_type,st_suffix,addr_2,apt_room,latitude,longitude,inci_type,clr_date,clr_time,alarms,complete,StartDate,EndDate,OBJECTID&outSR=4326&f=json')
        incident = allIncidents[0].json()
        print(allIncidents.json())
        return allIncidents.json()'''


class neighborhood_cirme(models.Model):


    url =' https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/NEIGHBORHOOD_CRIME_STATS/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'

    neighborhood = models.CharField(max_length=200)
    number = models.IntegerField()
    reportMonth = models.DateTimeField()
    reportYear = models.DateTimeField()
    urcDescription = models.CharField()

    def __str__(self):
        return f'{self.neighborhood}, on{self.reportMonth}, in {self.reportYear} this {self.urcDescription} Was reported by the Police.'


    def crimeReport():

        allCrimeReport = requests.get('https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/NEIGHBORHOOD_CRIME_STATS/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
        crimes = allCrimeReport[0].json()
        print(allCrimeReport.json())
        return crimes

            