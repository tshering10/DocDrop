from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import CustomUserCreationForm, ProfileForm
from  django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

#signup view
@login_required
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
@login_required
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
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-view')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_edit.html', {'form':form})

## profile delete view
@login_required
def profile_delete_view(request):
    user = request.user
    
    if request.method == 'POST':
        user.delete()
        return redirect('login')
    return render(request, 'accounts/profile_confirm_delete.html')
        