from django.urls import path
from accounts.views import (
    signup_view, login_view, logout_view,
    profile_view, profile_edit_view, profile_delete_view,
    settings_view,
)
urlpatterns = [
    path('signup/', signup_view, name="signup"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name='logout'),
    
    path('profile/', profile_view, name="profile-view"),
    path('profile/edit/', profile_edit_view, name="profile-edit"),
    path('profile/delete/', profile_delete_view, name="profile-delete"),
    
    path('settings/', settings_view, name="settings"),
]
