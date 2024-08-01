from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from Accounts.models import User


def myaccountdashboard(request):
    user = request.user
    if user.role ==1:
        return redirect('vdashboard')
    elif user.role == 2:
        return redirect('cdashboard')
    elif user.role == 3:
        return redirect('ddashboard')
    elif user.role == None and user.is_superadmin:
        return redirect ('/admin')
    else:
        raise PermissionDenied



