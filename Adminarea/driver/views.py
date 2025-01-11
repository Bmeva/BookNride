from Driver.models import driver
from django.shortcuts import redirect, render
from django.core.exceptions import PermissionDenied

from django.http import HttpResponse


def getalldriver(request):
    if not request.user.is_authenticated:
        return redirect('LoginView')
    if not request.user.is_admin:
        raise PermissionDenied
    else:
        thedriver = driver.objects.all()
        
        context = {
            'thedriver': thedriver,
        }
    return render(request, 'adminarea/admindriver/getalldriver.html', context)