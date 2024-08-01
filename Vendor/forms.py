from django import forms
from .models import vendor
from Accounts.validators import allow_only_images_validator



class vendorform(forms.ModelForm): 
    VendorLicense = forms.FileField(label='Vendor License',  help_text='Ppload your vendor license, image only', widget=forms.FileInput(attrs={'class': 'btn btn-danger'}), validators= [allow_only_images_validator]) #on the vprofile.htm we called the vendor license to display so this code would give the button a style css
    
           
    class Meta:
        model = vendor
        fields = ['VendorName', 'VendorLicense', 'vendorType']  
        
        widgets = {
            'VendorName': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Vendor Name'}),
            'vendorType': forms.Select(attrs={'class': 'contactus'}), 
            
                    
        }
        
        help_texts = {
            'vendorType': 'Please select your vendor type.'
        }

