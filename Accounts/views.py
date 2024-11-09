from django.shortcuts import render
from authentication.utility import send_verification_email, newuserEmail

# Create your views here.


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import userform
from django.contrib import messages
from Accounts.models import User

# Create your views here.

def registeruser(request):
    if request.user.is_authenticated: 
        messages.warning(request, "You are already logged in")
        return redirect('myaccountdashboard') 

    if request.method == 'POST':
        form = userform(request.POST) 
        if form.is_valid():
            password = form.cleaned_data['password'] 
            user = form.save(commit=False)
            user.set_password(password) 
            user.role = User.CUSTOMER
            user.save()
            
            #send verification email
            send_verification_email(request, user)
            newuserEmail(request, user)

            messages.success(request, "Your account has been registered successfully")
            return redirect('LoginView')  # Redirect to signin page after successful registration
        else:
            messages.error(request, "There was an error with your form submission. Please correct the errors below.")
            print("invalid form")
            print(form.errors)
    else:
        form = userform()
       

    context = {
        'form': form,
    }

    return render(request, 'accounts/userReg.html', context)
