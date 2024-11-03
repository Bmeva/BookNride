from django.db import models

# Create your models here.

from django.db import models
from Accounts.models import User, UserProfile

# Create your models here.

Vehicle_type = (
    ('Bike', 'Bike'),
    ('Car', 'Car'),
     
    
)


class driver(models.Model):
    user = models.OneToOneField(User, related_name='theuser', on_delete=models.CASCADE)
    User_Profile = models.OneToOneField(UserProfile, related_name='thedriverProfile', on_delete=models.CASCADE)
    driver_plate_reg = models.CharField(max_length=100)
    vehilce_type = models.CharField(max_length=100, choices=Vehicle_type)
    driverSlug = models.SlugField(max_length=100, unique=True)
    DriverLicense = models.ImageField(upload_to='driver/license')
    IsApproved = models.BooleanField(default=False)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    ModifiedAt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Driver'
        

    def __str__(self):
        return f"{self.driver_plate_reg} - {self.user.username}"

       
   