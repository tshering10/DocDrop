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
        
        
    def clean_file(self):
        file = self.cleaned_data.get('file')
        
        if not file:
            return file  # skip if no file uploaded (optional)

        # File size validation (max 20 MB)
        if file.size > 20 * 1024 * 1024:
            raise forms.ValidationError("File too large. Max size is 20 MB.")
        
        # File extension validation
        ext = os.path.splitext(file.name)[1]  # correct way to get extension
        valid_extensions = ['.pdf', '.docx', '.jpeg', '.jpg', '.txt', '.png']
        
        if ext.lower() not in valid_extensions:
            raise forms.ValidationError("Unsupported file extension.")
        
        return file