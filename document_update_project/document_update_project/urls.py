# project_name/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('document_update.urls')), 
    path('admin/', admin.site.urls),
]
