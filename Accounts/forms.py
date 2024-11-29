from django import forms
from .models import User, UserProfile

class userform(forms.ModelForm):
    
    #there is no confirm password and confirm password field in the User model so we would create custom fields for them
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'contactus', 'placeholder': 'Password'})) 
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'contactus', 'placeholder': 'Confirm Password'}), help_text="Your password must contain at least 8 characters.") 
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'role'] 
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Email'}),
            'role': forms.Select(attrs={'class': 'contactus'}), 
           
           
        }
        help_texts ={
            'role': 'Please select vendor role.',
        }
      

    def clean(self):
        cleaned_data = super(userform, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords does not match')
        


class adminuserform(forms.ModelForm):
       
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'role'] 
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Email'}),
            'role': forms.Select(attrs={'class': 'contactus'}), 
           
           
        }
        help_texts ={
            'role': 'Please select vendor role.',
        }
         
        


class Profileform(forms.ModelForm):
     
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'cover_photo', 'phone_number', 'post_code', 'disabled', 'bio', 'occupation', 'address_line_1', 'address_line_2', 'country', 'state', 'city', 'pin_code', 'latitude', 'longitude' ] 
        
        widgets = {
            'post_code': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Post Code'}),
            'phone_number': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Phone Number'}),
            'bio': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Type your Bio'}),
            'occupation': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Occupation'}),
            'address_line_1': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Adress 1'}),
            'address_line_2': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Adress 2'}),
            'country': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Country'}),
            'state': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'State'}),
            'city': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'city'}),
            'pin_code': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'pin code'}),
            'latitude': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'latitude'}),
            'longitude': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'longitude'}),
        
           
        }
        help_texts = {
            'disabled': 'Check this box to disable the user'
        }
        

