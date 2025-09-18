from django.urls import path
from files.views import dashboard, file_upload_view, user_dashboard, delete_view

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('upload/', file_upload_view, name="file-upload"),
    path('upload/my-files/', user_dashboard, name="my-uploads"),
    path('dashboard/delete/<int:id>/', delete_view, name="delete-file"),
]
