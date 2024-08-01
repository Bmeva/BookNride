from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .utility import myaccountdashboard



#        

def login(request):
    if request.user.is_authenticated:
        messages.warning(request, "you are already logged in")
        return redirect('myaccountdashboard')
    
    
   
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
          
        if not email:
            messages.error(request, 'email field cannot be empty')
        elif not password:
            messages.error(request, 'Password field cannot be empty')
        
        else:
            user = auth.authenticate(email=email, password=password) #This checks for the user with the email and password
        #the auth.authenticate comes from django.contrib
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'you are now logged in')
                return redirect('myaccountdashboard')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')


    return render(request, 'Auth/authentication.html')




# def myaccountdashboard(request):
#     user = request.user
#     if user.role ==1:
#         return redirect('vdashboard')
#     elif user.role == 2:
#         return redirect('cdashboard')
#     elif user.role == 3:
#         return redirect('ddashboard')
#     elif user.role == None and user.is_superadmin:
#         return redirect ('/admin')


def logout(request):
    auth.logout(request)
    messages.info(request, "you are now logged out")
    return redirect('home')