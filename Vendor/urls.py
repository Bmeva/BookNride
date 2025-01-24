
from django.urls import path
from .import views


urlpatterns = [
   
    path('vendorreg/', views.vendorreg, name='vendorreg'),
      
    path('vdashboard/', views.vdashboard, name='vdashboard'),
    
     path('vprofilemgt/', views.vprofilemgt, name='vprofilemgt'),
     
     
    
     
  
    
] 