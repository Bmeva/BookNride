from django.db import models
from Accounts.models import User, UserProfile
from authentication.utility import send_approval_notification_email

# Create your models here.

Vendor_type = (
    ('Individual', 'Individual'),
    ('Business', 'Business'),
     
    
)


class vendor(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    User_Profile = models.OneToOneField(UserProfile, related_name='theuserProfile', on_delete=models.CASCADE)
    VendorName = models.CharField(max_length=50)
    vendorType = models.CharField(max_length=50, choices=Vendor_type, default='Individual')
       
    VendorSlug = models.SlugField(max_length=50, unique=True)
    VendorLicense = models.ImageField(upload_to='vendor/license')
    IsApproved = models.BooleanField(default=False, help_text="Vendor approval")
    mail_approval_subject = models.CharField(max_length=200, null=True, blank=True)
    mail_approval_body = models.TextField(null=True, blank=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    ModifiedAt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendor'
        

    def __str__(self):
        return self.VendorName
    
    
    def save(self, *args, **kwargs): #gets tiggered when the save button is clicked on the admin 
        #dashboard. it checks the approval status of the is_approved for the vendor and sends a mail

        if self.pk is not None:
            #update
            orig = vendor.objects.get(pk=self.pk)
            if orig.IsApproved != self.IsApproved:
                mail_template = 'Accounts/emails/admin_approval_email.html'
                context = {
                    'user': self.user,
                    'is_approved': self.IsApproved,
                    'to_email': self.user.email,
                    'subject': self.mail_approval_subject,  
                    'body': self.mail_approval_body,       
                }

                if self.IsApproved:
                    mail_subject = self.mail_approval_subject if self.mail_approval_subject else "Congrats you have been approved as a vendor"
                else:
                    mail_subject = self.mail_approval_subject if self.mail_approval_subject else "Your vendor application has been rejected"

                # Send notification email
                send_approval_notification_email(mail_subject, mail_template, context)

        return super(vendor, self).save(*args, **kwargs) #the super funtion allows you to access
    #the save methord of the vendor class

       
   