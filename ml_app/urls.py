from django.contrib import admin
from django.urls import path
from django.urls import path,include
from ml_app import views
urlpatterns = [
    path('', views.predict, name='predict'),
    
]
