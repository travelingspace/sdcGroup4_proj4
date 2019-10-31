from django.urls import path
from . import views
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.home, name='home'),
    path('main/<int:zip_code>', views.main, name='main'),
    path('getZip/$', views.getZipFromLatLong, name='getZip'),
    path('cachedZips/', views.getAllZips, name='cachedZips'),
    path('addZip/<int:zip_code>', csrf_exempt(views.addZip), name='addZip'),
]