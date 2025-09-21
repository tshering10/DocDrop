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
    query = request.GET.get('q')
    
    if query:
        files = files.filter(title__icontains=query)
        
    return render(request, 'files/dashboard.html', {'files': files, 'query':query})

@login_required
def user_dashboard(request):
    user_files = File.objects.filter(uploader=request.user)
    return render(request, 'files/user_dashboard.html', {'user_files': user_files})

@login_required
def delete_view(request, id):
    file = get_object_or_404(File, id=id, uploader=request.user)
    file.delete()
    return redirect('dashboard')


@login_required
def details_view(request, id):
    file = get_object_or_404(File, id=id)
    return render(request, "files/file_detail.html", {"file":file})