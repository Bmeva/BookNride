from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.core.exceptions import PermissionDenied
from Accounts.models import User


def getallcustomers(request):
    if not request.user.is_authenticated:
        return redirect('LoginView')
    if not request.user.is_admin:
        raise PermissionDenied
    else:
        allcustomer = User.objects.filter(role=User.CUSTOMER)
        #if i wanted to query all records in the User model then i need to say
        # allcustomer = User.objects.all()
        
        
        context = {
            'allcustomer': allcustomer,
        }

    
    return render(request, 'adminarea/admincustomer/getallcustomer.html', context)

