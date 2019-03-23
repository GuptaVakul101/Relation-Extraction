from django.contrib import admin
from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('', views.index, name='index'),
    path('fillData', views.fill_data, name='fill_data'),
]
