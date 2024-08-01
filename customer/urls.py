from django.urls import path
from .import views


urlpatterns = [
     
    path('cdashboard/', views.cdashboard, name='cdashboard'),
    
    
    
] 