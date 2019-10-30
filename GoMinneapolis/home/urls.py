from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main/<int:zip_code>', views.main, name='main')
]