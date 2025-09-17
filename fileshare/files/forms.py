from django import forms
from .models import File
import os
class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['title', 'file', 'category']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'px-3 py-2 mt-1 mb-3 border border-gray-800 rounded-lg bg-gray-800 text-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': "Name the file.."
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': 'px-3 py-2 mt-1 mb-3 border border-gray-800 rounded-lg bg-gray-800 pointer  text-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500'
            })
        }
        
        
    def clean(self):
        file = self.cleaned_data.get('file')
        
        #file size validation
        if file.size > 20 * 1024 * 1024:
            raise forms.ValidationError("File too large.Max size is 20 MB.")
        
        # file extension validation
        ext = os.path.split(file.name)[1]
        valid_extensions = ['.pdf', '.docx', '.jpeg', '.jpg', '.txt', '.png']
        
        if ext.lower() not in valid_extensions:
            raise forms.ValidationError("Unsupported file extension.")
        
        return file