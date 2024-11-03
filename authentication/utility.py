from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from Accounts.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages




def myaccountdashboard(request):
    user = request.user
    if user.role ==1:
        return redirect('vdashboard')
    elif user.role == 2:
        return redirect('cdashboard')
    elif user.role == 3:
        return redirect('ddashboard')
    elif user.role == None and user.is_superadmin:
        return redirect ('get_all_vendor')
        #return redirect ('/admin') using this would log into the admin panel
    
    
    else:
        raise PermissionDenied
    
    



def send_verification_email(request, user):
    from_email = settings.DEFAULT_FROM_EMAIL 
    current_site = get_current_site(request)
    mail_subject = "Please activate your account"
    message = render_to_string('Accounts/emails/account_verification_email.html', {

        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
      
        

    })
    to_email = user.email
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.content_subtype = "html"
    mail.send()
    



def newuserEmail(request, user):
    from_email = settings.DEFAULT_FROM_EMAIL 
    current_site = get_current_site(request)
    mail_subject = "New User Alert"
    message = render_to_string('Accounts/emails/new_user_email.html', {

        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
      

    })
    
    admin_user = User.objects.filter(is_superadmin =True).first()
    if admin_user:
        to_email = admin_user.email
    else:
        # If no superuser is found, default to a configured email (optional)
        to_email = 'evansboma@gmail.com'
        
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.content_subtype = "html"
    mail.send()
    


def activate(request, uidb64, token):
    #activating the user by setting the is_active status to true
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk = uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Congratulations your account has been activated")
        return redirect('LoginView')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('LoginView')
    


from django.utils.timezone import now
def activate(request, uidb64, token):
    try:
        # Decode the UID from the URL
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # Check if user exists and the token is valid
    if user is not None and default_token_generator.check_token(user, token):
        # If the user is already activated, handle the case
        if user.is_active:
            messages.info(request, "Your account is already activated.")
            return redirect('LoginView')

        # Check if the token has expired based on the defined timeout
        token_age = (now() - user.date_joined).total_seconds()
        if token_age > settings.PASSWORD_RESET_TIMEOUT:
            messages.error(request, "Your activation link has expired. Please request a new activation link.")
            send_verification_email(request, user)
            #return redirect('resend_activation_link')  # Provide a route to request a new activation link

        # Activate user account
        user.is_active = True
        user.save()
        messages.success(request, "Your account has been activated successfully!")
        return redirect('LoginView')
    else:
        messages.error(request, "Invalid activation link.")
        return redirect('LoginView')

     
 

def send_password_reset_email(request, user):
    
    from_email = settings.DEFAULT_FROM_EMAIL 
    current_site = get_current_site(request)
    mail_subject = "reset your password"
    message = render_to_string('Auth/Resetpassword/reset_password_email.html', {

        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),

    })
    to_email = user.email
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.send()

    


def send_approval_notification_email(mail_subject, mail_template, context):
    from_email = settings.DEFAULT_FROM_EMAIL
    message = render_to_string(mail_template, context)
    if(isinstance(context['to_email'], str)):
        to_email = []
        to_email.append(context['to_email'])
    else:
        to_email = context['to_email']
    mail = EmailMessage(mail_subject, message, from_email, to=to_email)
    mail.content_subtype = "html"
    mail.send()

    return


# this code assumes if the role is defined in the UserProfile model
# from Accounts.models import UserProfile

# from django.core.exceptions import PermissionDenied

# def myaccountdashboard(request):
#     user = request.user  # Get the currently logged-in user
    
#     try:
#         profile = UserProfile.objects.get(user=user)  # Get the UserProfile for the current user
#     except UserProfile.DoesNotExist:
#         raise PermissionDenied("Profile does not exist")

#     # Redirect based on role
#     if profile.role == UserProfile.VENDOR:
#         return redirect('vdashboard')
#     elif profile.role == UserProfile.CUSTOMER:
#         return redirect('cdashboard')
#     elif profile.role == UserProfile.DRIVER:
#         return redirect('ddashboard')
#     elif profile.role is None and user.is_superuser:  # Ensure you're checking the correct attribute
#         return redirect('/admin')
#     else:
#         raise PermissionDenied("You do not have permission to access this page")


