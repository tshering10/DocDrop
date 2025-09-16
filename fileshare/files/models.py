from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class File(models.Model):
    CATEGORY_CHOICES = [
        ('notes', 'Notes'),
        ('guides', 'Guides'),
        ('assignments', 'Assignments'),
        ('others', 'Others'),
    ]
    
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='others')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title