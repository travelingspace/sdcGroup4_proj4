from django.db import models

# Create your models here.
class FireReport(model.Model):
    inci_no = models.CharField()
    description = models.CharField()
    alm_date = models.DateField()
    alm_time = models.TimeField()
    building_num = models.CharField()
    street_num = models.CharField()
    lattitude = models.DecimalField()
    longitude = models.DecimalField()
    incident_type = models.CharField()

    def _str_(self):
        return f'{self.inci_no}, on {self.alm_date} at {self.alm_time} was reported at location address {self.building_num}, {self.street_num}. It was of incident type {self.incident_type}.'