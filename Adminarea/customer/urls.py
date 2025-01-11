from django.urls import path
from .import views


urlpatterns = [
    path('', views.getallcustomers, name='getallcustomers'),
    #to view this directly typing url http://127.0.0.1:8082/adminarea/customeradmin/
    
    path('getallcustomers/', views.getallcustomers, name='getallcustomers'),
    #To view this directly typing the url http://127.0.0.1:8080/adminarea/customeradmin/getallcustomers/
    
]