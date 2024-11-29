from django.urls import path
from .import views


urlpatterns = [
    
      
    path('', views.get_all_vendor, name='get_all_vendor'),
 
         
    path('get_all_vendor/', views.get_all_vendor, name='get_all_vendor'),
    
      
    path('delete_vendor/<int:pk>/', views.delete_vendor, name='delete_vendor'),
    
    path('admin_update_vendor/<int:pk>/', views.admin_update_vendor, name='admin_update_vendor'),
    
    
    path('admin_update_vendor_password/<int:pk>/', views.admin_update_vendor_password, name='admin_update_vendor_password'),
    
      
    path('errorpage/', views.errorpage, name='errorpage'),
    
    
    path('get_single_vendor/<int:pk>/', views.get_single_vendor, name='get_single_vendor'),
    
    
 
    
 
    
    
] 