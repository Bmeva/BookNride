
from django.urls import path
from .import views


urlpatterns = [
   
    path('driver/', views.driverreg, name='driverreg'),
    
    path('ddashboard/', views.ddashboard, name='ddashboard'),
     
  
    
] 