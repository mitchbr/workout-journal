from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls), 
    path("", include("workouts.urls", namespace='workouts')),
    path("", include('pwa.urls')),
]
