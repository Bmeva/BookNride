from django import forms
from .models import driver
from Accounts.validators import allow_only_images_validator



class driverform(forms.ModelForm): 
    DriverLicense = forms.FileField(label='Vendor License',  help_text='Ppload your vendor license, image only', widget=forms.FileInput(attrs={'class': 'btn btn-danger'}), validators= [allow_only_images_validator]) #on the vprofile.htm we called the vendor license to display so this code would give the button a style css
    
           
    class Meta:
        model = driver
        fields = ['driver_plate_reg', 'DriverLicense', 'vehilce_type']  
        
        widgets = {
            'driver_plate_reg': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Enter your plate number'}),
            'vehilce_type': forms.Select(attrs={'class': 'contactus'}), 
            
                    
        }
        
        help_texts = {
            'vehilce_type': 'Please select your vehicle type.'
        }

