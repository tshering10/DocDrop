from django import forms
from .models import File
import os
class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['title', 'file', 'category']
        
    def clean(self):
        file = self.clean_data.get('file')
        
        #file size validation
        if file.size > 20 * 1024 * 1024:
            raise forms.ValidationError("File too large.Max size is 20 MB.")
        
        # file extension validation
        ext = os.path.split(file.name)[1]
        valid_extensions = ['.pdf', '.docx', '.jpeg', '.jpg', '.txt', '.png']
        
        if ext.lower() not in valid_extensions:
            raise forms.ValidationError("Unsupported file extension.")
        
        return file