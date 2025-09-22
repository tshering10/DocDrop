from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"