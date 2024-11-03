from django import forms
from .models import vendor
from Accounts.validators import allow_only_images_validator



class vendorform(forms.ModelForm): 
    VendorLicense = forms.FileField(label='Vendor License',  help_text='Please your vendor license, image only', widget=forms.FileInput(attrs={'class': 'btn btn-danger'}), validators= [allow_only_images_validator]) #on the vprofile.htm we called the vendor license to display so this code would give the button a style css
    
           
    class Meta:
        model = vendor
        fields = ['VendorName', 'VendorLicense', 'vendorType', 'IsApproved', 'mail_approval_subject', 'mail_approval_body' ]  
        
        widgets = {
            'VendorName': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Vendor Name'}),
            'mail_approval_subject': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Enter mail subject'}),
            'mail_approval_body': forms.Textarea(attrs={'class': 'contactus', 'placeholder': 'Enter mail Body'}),
            'vendorType': forms.Select(attrs={'class': 'contactus'}), 
            
                    
        }
        
        help_texts = {
            'vendorType': 'Please select vendor type.',
            'mail_approval_subject': 'subject is optionl and you can use default subject',
            'mail_approval_body': 'Mail body is optional and you can use default mail body',
            'IsApproved': 'Check this box if the vendor is approved.'
                  
            
        }
    
      

