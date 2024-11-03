from django import forms
from .models import User

class userform(forms.ModelForm):
    
    #there is no confirm password and confirm password field in the User model so we would create custom fields for them
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'contactus', 'placeholder': 'Password'})) 
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'contactus', 'placeholder': 'Confirm Password'}), help_text="Your password must contain at least 8 characters.") 
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'post_code', 'phone_number', 'password', 'bio'] 
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Email'}),
            'post_code': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Post Code'}),
            'phone_number': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Phone Number'}),
            'bio': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Type your Bio'}),
                      
           
        }


    def clean(self):
        cleaned_data = super(userform, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords does not match')