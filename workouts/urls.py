from django.urls import path
from . import views

app_name = 'workouts'

urlpatterns = [
    path('', views.index, name='index'),
    path('workout/<int:workout_id>/', views.update_workout, name='update_workout'),
    path('workout', views.workout, name='workout'),
    path('workout/fields/', views.get_workout_type_fields, name='workout_type_fields'),
    path('workout/modal/<int:workout_id>/', views.get_workout_modal, name='workout_modal'),
]
