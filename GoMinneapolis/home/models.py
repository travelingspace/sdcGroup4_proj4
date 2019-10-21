from django.db import models

# Create your models here.
class FireReport(models.Model):
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