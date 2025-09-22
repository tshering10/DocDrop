from django.contrib import admin
from accounts.models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', "profilePicture", "joined_at", "updated_at")
    search_fields = ("user__username", "user__email")
    list_filter = ("joined_at",)
    
admin.site.register(Profile, ProfileAdmin)