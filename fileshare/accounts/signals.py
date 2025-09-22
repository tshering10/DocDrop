from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from accounts.models import Profile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # create profile for new users
        Profile.objects.create(user=instance)
    else:
        # save profile for existing users
        instance.profile.save()   
