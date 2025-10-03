from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError("Username must be at least 3 characters long.")
        return username
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password1 = cleaned_data.get('password1')
    #     password2 = cleaned_data.get('password2')
        
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords did not match.")
    #     return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "w-full px-3 py-2 rounded-md bg-gray-800 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Enter username"
        })
        self.fields["email"].widget.attrs.update({
            "class": "w-full px-3 py-2 rounded-md bg-gray-800 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Enter email"
        })
        self.fields["password1"].widget.attrs.update({
            "class": "w-full px-3 py-2 rounded-md bg-gray-800 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Enter password"
        })
        self.fields["password2"].widget.attrs.update({
            "class": "w-full px-3 py-2 rounded-md bg-gray-800 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Confirm password"
        })

class CustomAuthenticationForm(AuthenticationForm):

    error_messages = {
        'invalid_login': (
            "Invalid login credentials. Please check your username and password."
        ),
        'inactive': "This account is inactive.",
    }
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profilePicture']
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']