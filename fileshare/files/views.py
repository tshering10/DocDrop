from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import File
from .forms import FileUploadForm
@login_required
def file_upload_view(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.uploader = request.user
            file_instance.save()
            return redirect('dashboard')
    else:
        form = FileUploadForm()
    return render(request, "files/upload.html", {"form": form})

#dashboard
@login_required
def dashboard(request):
    files = File.objects.all().order_by('-uploaded_at')
    return render(request, 'files/dashboard.html', {'files': files})

@login_required
def user_dashboard(request):
    user_files = File.objects.filter(uploader=request.user)
    return render(request, 'files/user_dashboard.html', {'user_files': user_files})

def delete_view(request, id):
    file = get_object_or_404(File, id=id, uploader=request.user)
    file.delete()
    return redirect('dashboard')
