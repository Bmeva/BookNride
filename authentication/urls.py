from django.urls import path
from .import views

from .views import LoginView 


urlpatterns = [
    
    path('LoginView/', LoginView.as_view(), name='LoginView'),
     
    #path('login/', views.login, name='login'),
    
    path('logout/', views.logout, name='logout'),
    
    
    path('video/', views.video, name='video'),
      
    
    path('myaccountdashboard/', views.myaccountdashboard, name='myaccountdashboard'),
    #this url works becouse in my views i imported myaccountdashboard evenn though there is no 
    #myaccountdashboard function in views.py
    
    path('forgot_password', views.forgot_password, name = 'forgot_password'),
    
    path('reset_password_validate/<uidb64>/<token>/', views.reset_password_validate, name='reset_password_validate'),
    path('reset_password/', views.reset_password, name='reset_password'),


    
    
     
    
] 