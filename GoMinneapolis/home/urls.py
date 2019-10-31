from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    path('main/<int:zip_code>', views.main, name='main'),
    path('getZip/$', views.getZipFromLatLong, name='getZip'),
    path('cachedZips/', views.getAllZips, name='cachedZips')
]