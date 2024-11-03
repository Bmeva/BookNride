from django.urls import path
from .import views
from authentication import utility


urlpatterns = [
     
    path('registeruser/', views.registeruser, name='registeruser'),
    
     path('activate/<uidb64>/<token>/', utility.activate, name='activate'),
    
    
    
] 