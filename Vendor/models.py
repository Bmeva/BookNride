from django.db import models
from Accounts.models import User, UserProfile

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
    IsApproved = models.BooleanField(default=False)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    ModifiedAt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendor'
        

    def __str__(self):
        return self.VendorName

       
   