from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('', include('applications.home.urls')),
    path('', include('applications.biblioteca.urls')),
    path('admin/', admin.site.urls),
]
