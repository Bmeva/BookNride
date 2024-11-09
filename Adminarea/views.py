from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from Vendor.models import vendor
from Vendor.forms import vendorform
from Accounts.forms import userform
from Accounts.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

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
        thevendor = get_object_or_404(vendor, pk=pk)
        thevuser = thevendor.user
        #thevenprofile = thevendor.User_Profile would use this to enable admin update the profile as well        
    except vendor.DoesNotExist:
        messages.error(request, 'Vendor account does not exist')
        return redirect('get_all_vendor')
    
  

    if request.method == 'POST':
        thevendorupdate = vendorform(request.POST, request.FILES, instance=thevendor)
        theuserupdate = userform(request.POST, request.FILES, instance=thevuser)
        
        if thevendorupdate.is_valid() and theuserupdate.is_valid():
            thevendorupdate.save()
            theuserupdate.save()
            messages.success(request, 'Vendor details have been updated')
            return redirect('admin_update_vendor', pk=pk)  # Redirect to the same vendor update page
    else:
        thevendorupdate = vendorform(instance=thevendor)
        theuserupdate = userform(instance=thevuser)
        
    context = {
        'thevendor': thevendor,
        'thevendorupdate': thevendorupdate,
        'theuserupdate': theuserupdate,
        'thevuser': thevuser,
    }
    
    return render(request, 'adminarea/admin_update_vendor.html', context)



def delete_vendor(request, pk):
    thevendor = get_object_or_404(vendor, pk=pk)
    thevendor.delete()
    messages.success(request, 'vendor has been deleted')
    
    return redirect('get_all_vendor')


def errorpage(request):
    return render(request, 'adminarea/errorpage.html')