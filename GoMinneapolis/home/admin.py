from django.contrib import admin
from .models import LiquorSales
from .models import ZipCode

# Register your models here.
admin.site.register(LiquorSales)
admin.site.register(ZipCode)