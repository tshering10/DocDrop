from django.urls import path
from files.views import dashboard, file_upload_view, user_dashboard

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('upload/', file_upload_view, name="file-upload"),
    path('upload/my-files/', user_dashboard, name="my-uploads"),
]
