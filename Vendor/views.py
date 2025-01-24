from django.shortcuts import render, redirect
from django.contrib import messages
from Accounts.forms import userform
from Vendor.forms import vendorform
from Accounts.models import User, UserProfile
from django.template.defaultfilters import slugify

from authentication.utility import myaccountdashboard
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from authentication.utility import send_verification_email
from authentication.utility import newuserEmail
from django.shortcuts import get_object_or_404
from .models import vendor
from Accounts.forms import Profileform
from django.http import Http404
from Accounts.forms import user_form_withoutpassword
# Create your views here.

#return HttpResponse("This is the user registration page")
# from django.shortcuts import render, redirect, HttpResponse
def vendorreg(request):
    if request.user.is_authenticated: 
         messages.warning(request, "you are already logged in")
         return redirect('home')
    
    elif request.method =='POST':
        form = userform(request.POST)
        v_form = vendorform(request.POST, request.FILES)
        if form.is_valid() and v_form.is_valid():
            password = form.cleaned_data['password'] 
            user = form.save(commit=False)
            user.set_password(password) 
            user.role = User.VENDOR
            user.save()
            
                       
            vendor = v_form.save(commit=False)
            vendor.user = user
            theVendorName = v_form.cleaned_data['VendorName']
            vendor.VendorSlug = slugify(theVendorName) + '-'+str(user.id) 
            theUser_Profile = UserProfile.objects.get(user=user)
            vendor.User_Profile = theUser_Profile
            vendor.save()
            
            send_verification_email(request, user)
            newuserEmail(request, user)
            
            messages.success(request, "Your account has been registered succesfully, please wait for approval")
            
            
            #you can also use message without error or warning or info just message = "Please enter a search term."
            return redirect('LoginView')


        else:
            print('invalid form')
            print(form.errors)
     
    else:
        form = userform()
        v_form = vendorform()
    

    context = {

        'form': form,
        'v_form': v_form,
    }
       
    return render(request, 'vendor/vendorreg.html', context)


#@login_required(login_url = 'login') 
def vdashboard(request):
    if not request.user.is_authenticated:
        return redirect('LoginView') 
    
    if request.user.role != 1:
         #return HttpResponse("You are not authorised to view this page")
        raise PermissionDenied #I added a 403.html so it would display the content inside the 403.html. otherwise it would display the default notification
    
    thevendor = get_object_or_404(vendor, user= request.user)
    
    duser = thevendor.User_Profile
    #duser = UserProfile.objects.get(user = request.user) this would also work
    
    context ={
        'thevendor': thevendor,
        'duser': duser,
    }
    
    return render (request, 'vendor/vdashboard.html', context )

# def vendorreg(request):
#     if request.user.is_authenticated: 
#         messages.warning(request, "you are already logged in")
#         return redirect('myaccount')
    
#     elif request.method =='POST':
#         form = userform(request.POST)
#         v_form = vendorform(request.POST, request.FILES)
        
#         if form.is_valid() and v_form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             phone_number = form.cleaned_data['phone_number']
#             password = form.cleaned_data['password']
#             #confirm_password = form.cleaned_data['confirm_password']
#             user = User.objects.create_user(
#                 first_name=first_name, 
#                 last_name=last_name, 
#                 username=username, 
#                 email=email, 
#                 phone_number=phone_number, 
#                 password=password, 
#                 #confirm_password=confirm_password
#                 )
#             user.role = User.VENDOR
#             user.save()
#             vendor = v_form.save(commit=False)
#             vendor.user = user
#             vendor_name = v_form.cleaned_data['vendor_name']
#             vendor.vendor_slug = slugify(vendor_name) + '-'+str(user.id) #if a user tries to register a vendor name that already exist then concatenating the user id would make it unique
#             user_profile = UserProfile.objects.get(user=user)
#             vendor.user_profile = user_profile
#             vendor.save()

           

#             messages.success(request, "Your account has been registered succesfully, please wait for approval")
#             return redirect(vendorreg)

#         else:
#             print("invalid form")
#             print(form.errors, v_form.errors)

#     else:
#         form = userform()
#         v_form = vendorform()

#     context = {

#         'form': form,
#         'v_form': v_form,
#     }
       
#    return render(request, 'accounts/userReg.html', context)



    
   


def vprofilemgt(request):
    try:
             
        theuser = request.user
        theven = vendor.objects.get(user = theuser)
        thvenprofile = theven.User_Profile
    except User.DoesNotExist:
        return redirect('LoginView')
    except vendor.DoesNotExist:
        raise Http404('your vendor account no longer exist')
    except UserProfile.DoesNotExist:
        raise Http404('your profile no longer exist')
        
   
        messages.error(request, 'user profile does not exist')
        return redirect(request, 'vdashboard')
 
    if request.method == 'POST':
        thevendorupdate = vendorform(request.POST, request.FILES, instance=theven)
        theprofileupdate = Profileform(request.POST, request.FILES, instance=thvenprofile)
        theuserupdate = user_form_withoutpassword(request.POST, request.FILES, instance=theuser)
      
        if thevendorupdate.is_valid() and theprofileupdate.is_valid() and theuserupdate.is_valid():
            user = theuserupdate.save(commit=False)
            user.role = User.VENDOR
            
            thevendorsave = thevendorupdate.save(commit=False)
            thevendorsave.IsApproved = True
            
            
            user.save()
            thevendorupdate.save()
            theprofileupdate.save()
            
            
            messages.success(request, 'Your details have been updated')
            return redirect('vprofilemgt')
    else:
        thevendorupdate = vendorform(instance=theven)
        theprofileupdate = Profileform(instance=thvenprofile)
        theuserupdate = user_form_withoutpassword(instance=theuser)
       
       
    context = {
        'thevendorupdate': thevendorupdate,
        'theprofileupdate': theprofileupdate,
        'theuserupdate': theuserupdate,
        'theven': theven,
        
       
    }
    
    return render(request, 'vendor/vprofilemgt.html', context)
#in this code i used try but its not necesary bcos they must have logged into their account and 
#authenticated before they can see the dashboard. However another admiin can delete an account so
#the try block becomes neccesary