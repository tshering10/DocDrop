from django.db import models
from django.contrib.auth.models import  User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilePicture = models.ImageField(
        upload_to="profile_pictures",
        default="profile_pictures/default.png",
        blank=True,
        null=True
        )
    joined_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    