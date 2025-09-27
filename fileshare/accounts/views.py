from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import CustomUserCreationForm, ProfileForm, UserForm
from  django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

#signup view
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

#login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

#logout view
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

#profile view
@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, "accounts/profile_view.html", {'profile':profile})


# profile edit view
@login_required
def profile_edit_view(request):
    user = request.user
    profile = user.profile
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile-view')
        else:
            print(profile_form.errors)
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)
        
    return render(request, 'accounts/profile_edit.html', {
        'profile_form':profile_form,
        'user_form': user_form
        })

## profile delete view
@login_required
def profile_delete_view(request):
    user = request.user
    
    if request.method == 'POST':
        user.delete()
        return redirect('login')
    return render(request, 'accounts/profile_confirm_delete.html')
        
@login_required
def settings_view(request):
    return render(request, "accounts/settings.html")