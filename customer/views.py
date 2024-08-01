from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.

# @login_required(login_url = 'login') 
def cdashboard(request):
    if not request.user.is_authenticated: #instead of using the login decorator i can check if users are logged in and redirect them
        return redirect('login') 
    if request.user.role != 2:
         #return HttpResponse("You are not authorised to view this page")
        raise PermissionDenied #I added a 403.html so it would display the content inside the 403.html. otherwise it would display the default notification
    
    
    return render(request, 'Customer/Cdashboard.html')