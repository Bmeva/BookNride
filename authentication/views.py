from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .utility import myaccountdashboard, send_password_reset_email
from Accounts.models import User
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.views import View
from django.contrib.auth import login as auth_login

class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "You are already logged in")
            return redirect('myaccountdashboard')
        return render(request, 'Auth/authentication.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email:
            messages.error(request, 'Email field cannot be empty')
        elif not password:
            messages.error(request, 'Password field cannot be empty')
        else:
            user = auth.authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('myaccountdashboard')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('LoginView')

        return redirect('LoginView')



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

def video(request):
    
    return render(request, 'Auth/video.html')



def forgot_password(request):
    if request.method == 'POST':
        theemail = request.POST['email']
        if User.objects.filter(email = theemail).exists():
            theuser = User.objects.get(email__exact=theemail)
            #theuser = User.objects.get(email__iexact=theemail) this would be case sensitive
            #theuser = User.objects.filter(email=theemail): This will check if any user exists with that email, but it's generally case-insensitive in most databases.

            send_password_reset_email(request, theuser)
            messages.info(request, 'PAssword reset link has been sent')
            return redirect('LoginView')
        else:
            messages.error(request, 'there is no account associated with the email address')
            return render(request, 'Auth/Resetpassword/forgotpass.html')
        
    return render(request, 'Auth/Resetpassword/forgotpass.html')



def reset_password_validate(request, uidb64, token): 
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk = uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.info(request, 'Please reset your password')
        return redirect('reset_password')
    else:
        messages.error(request, "This link has expired")
        return redirect('myaccount')
    
     



def reset_password(request):

    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['password2']

        if not password:
            messages.error(request, 'Password field cannot be emty')
        elif len(password) < 6:
            messages.error(request, "Password must be 6 characters")
        elif not confirm_password:
            messages.error(request, "Confirm password field cannot be empty")
        
        elif password != confirm_password:
            messages.error(request, 'password fields do not match')

                 
        else:
            pk = request.session.get('uid') #the uid was gotten from the reset_password_validate function
            user = User.objects.get(pk = pk)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, 'Password reset succesful')
            return redirect('LoginView')

    return render(request, 'Auth/Resetpassword/reset_password.html')
