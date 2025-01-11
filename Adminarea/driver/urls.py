from django.urls import path
from .import views


urlpatterns = [
    path('', views.getalldriver, name ='getalldrivers'),
    
      
    path('getalldriver/', views.getalldriver, name ='getalldrivers')
]