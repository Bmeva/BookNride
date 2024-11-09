from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from Accounts.forms import userform
from Driver.forms import driverform
from Accounts.models import User, UserProfile
from django.template.defaultfilters import slugify
from authentication.utility import myaccountdashboard
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from authentication.utility import send_verification_email, newuserEmail
from django.shortcuts import get_object_or_404
from .models import driver




# Create your views here.

#return HttpResponse("This is the user registration page")
# from django.shortcuts import render, redirect, HttpResponse
def driverreg(request):
    if request.user.is_authenticated: 
         messages.warning(request, "you are already logged in")
         return redirect('myaccountdashboard')
    
    elif request.method =='POST':
        form = userform(request.POST)
        d_form = driverform(request.POST, request.FILES)
        if form.is_valid() and d_form.is_valid():
            password = form.cleaned_data['password'] 
            user = form.save(commit=False)
            user.set_password(password) 
            user.role = User.DRIVER
            user.save()
           
            
            driver = d_form.save(commit=False)
            driver.user = user
            theDriverPlateReg = d_form.cleaned_data['driver_plate_reg']
            driver.driverSlug = slugify(theDriverPlateReg) + '-'+str(user.id) 
            driverUser_Profile = UserProfile.objects.get(user=user)
            driver.User_Profile = driverUser_Profile
            driver.save()
            
            send_verification_email(request, user)
            newuserEmail(request, user)
            
            messages.success(request, "Your account has been registered succesfully, please wait for approval")
            return redirect('LoginView')


        else:
            print('invalid form')
            print(form.errors)
     
    else:
        form = userform()
        d_form = driverform()
    

    context = {

        'form': form,
        'd_form': d_form,
    }
       
    return render(request, 'Driver/driverreg.html', context)
   

#@login_required(login_url = 'login') 
def ddashboard(request):
    if not request.user.is_authenticated: #instead of using the login decorator i can check if users are logged in and redirect them
        return redirect('LoginView') 
    
    if request.user.role != 3:
        #return HttpResponse("You are not authorised to view this page")
        raise PermissionDenied  #I added a 403.html so it would display the content inside the 403.html. otherwise it would display the default notification
    
     
    thedriver = get_object_or_404(driver, user= request.user)
    dtheuser = request.user
   
    context ={
        'thedriver': thedriver,
        'dtheuser': dtheuser,
      
    }
    
    return render(request, 'Driver/ddashboard.html', context)
    