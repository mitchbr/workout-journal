from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls), 
    path('dump_db', views.dump_db, name='dump_db'),
    path("", include("workouts.urls", namespace='workouts')),
    path("", include('pwa.urls')),
]
