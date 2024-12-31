from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from Vendor.models import vendor
from Vendor.forms import vendorform
from Accounts.forms import userform, Profileform, adminuserform
from Accounts.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q

# Create your views here.


#@login_required(login_url='LoginView')
def get_all_vendor(request):
    
    if not request.user.is_authenticated:
        return redirect('LoginView')
     
    if not request.user.is_admin:
        
        raise PermissionDenied 
    else:
        
        
        allvendor = vendor.objects.all()
        
        context ={
            'allvendor': allvendor
    }
    return render(request, 'adminarea/vendor_view.html', context)


def get_single_vendor(request, pk):
    
    try:
        
        thevendor = vendor.objects.get(pk =pk)
    except vendor.DoesNotExist:
        
        return redirect('errorpage')
        #return HttpResponse('You are a fool')
    
    context = {
        'thevendor': thevendor
    }
    
    return render(request, 'adminarea/single_vendor_view.html', context)



def admin_update_vendor(request, pk):
    try:
        thevendor = get_object_or_404(vendor, pk=pk)# i created a 404 page so it redirects there if 
        #the obkect is not found. otherwise it would have used django default 404 page
        thevenprofile = thevendor.User_Profile 
        
        thevuser = thevendor.user
        
    
        
    except vendor.DoesNotExist:
        messages.error(request, 'Vendor account does not exist')
        return redirect('get_all_vendor')
    
  

    if request.method == 'POST':
        thevendorupdate = vendorform(request.POST, request.FILES, instance=thevendor)
        theprofileupdate = Profileform(request.POST, request.FILES, instance=thevenprofile)
       
        theuserupdate = adminuserform(request.POST, request.FILES, instance=thevuser)
        #i used another userform that excludes the password bcos on the page i dont want admin to update the password
        
        if thevendorupdate.is_valid() and theprofileupdate.is_valid() and theuserupdate.is_valid():
            thevendorupdate.save()
            theprofileupdate.save()
            theuserupdate.save()
            messages.success(request, 'Vendor details have been updated')
            return redirect('admin_update_vendor', pk=pk)  # Redirect to the same vendor update page
    else:
        thevendorupdate = vendorform(instance=thevendor)
        theprofileupdate = Profileform(instance=thevenprofile)
        theuserupdate = userform(instance=thevuser)
        
    context = {
        'thevendor': thevendor,
        'thevendorupdate': thevendorupdate,
        'theprofileupdate': theprofileupdate,
        'theuserupdate': theuserupdate,
        #'thevuser': thevuser,
    }
    
    return render(request, 'adminarea/admin_update_vendor.html', context)


def admin_update_vendor_password(request, pk):
    
    thevendor = get_object_or_404(vendor, pk=pk)
    thevuser = thevendor.user
        
    
   
    if request.method == 'POST':
        theuserupdate = userform(request.POST, instance=thevuser)
       
        if theuserupdate.is_valid():
            password = theuserupdate.cleaned_data['password'] 
            
            theuser = theuserupdate.save(commit=False)
            theuser.set_password(password)
           
            theuser.save()
            messages.success(request, f'Vendor {thevuser.first_name }details have been updated')
            return redirect('admin_update_vendor_password', pk=pk)  # Redirect to the same vendor update page
        else:
            messages.error(request, 'there is a problem updating the record')
    else:
        
        theuserupdate = userform(instance=thevuser)
        
    context = {
        'thevendor': thevendor,
    
        'theuserupdate': theuserupdate,
        #'thevuser': thevuser,
    }
    
    return render(request, 'adminarea/admin_update_vpassword.html', context)

def searchvendor(request):
    thesearchword = request.GET.get('searchword', '').strip()
    if thesearchword:
           
    
        thesearch = vendor.objects.filter(Q(VendorName__icontains = thesearchword)
                                      | Q(VendorSlug__icontains = thesearchword)
                                      | Q(user__email__icontains = thesearchword))
        message = None
        
    else:
        thesearch = vendor.objects.none()
        message = "Please enter search word"
    
    context = {
        'thesearch': thesearch,
        'message': message
    }
    
    
    
    return render(request, 'adminarea/search_vendor.html', context )


#on the userform i have already compared the password and confirm password otherwise i would 
#have used this approach below
# def admin_update_vendor_password(request, pk):
#     thevendor = get_object_or_404(vendor, pk=pk)
#     thevuser = thevendor.user

#     if request.method == 'POST':
#         theuserupdate = userform(request.POST, instance=thevuser)
        
#         if theuserupdate.is_valid():
#             # Extract the password and confirm_password fields
#             password = theuserupdate.cleaned_data.get('password')
#             confirm_password = theuserupdate.cleaned_data.get('confirm_password')

#             if password:  # Ensure the password is provided
#                 if password == confirm_password:  # Ensure passwords match
#                     theuser = theuserupdate.save(commit=False)
#                     theuser.set_password(password)  # Hash and set the password
#                     theuser.save()  # Save the user instance
#                     messages.success(request, f"Password for {thevendor.user.username} updated successfully.")
#                     return redirect('admin_update_vendor', pk=pk)
#                 else:
#                     messages.error(request, 'Passwords do not match.')
#             else:
#                 messages.error(request, 'Password cannot be empty.')
#         else:
#             # If the form is invalid, display errors
#             messages.error(request, 'There was a problem updating the password.')
#     else:
#         # Initialize the form
#         theuserupdate = userform(instance=thevuser)

#     context = {
#         'thevendor': thevendor,
#         'theuserupdate': theuserupdate,
#     }

#     return render(request, 'adminarea/admin_update_vpassword.html', context)

def delete_vendor(request, pk):
    thevendor = get_object_or_404(vendor, pk=pk)
    thevendor.delete()
    messages.success(request, 'vendor has been deleted')
    
    return redirect('get_all_vendor')


def errorpage(request):
    return render(request, 'adminarea/errorpage.html')