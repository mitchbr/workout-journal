from django.urls import path
from . import views

app_name = 'workouts'

urlpatterns = [
    path('', views.index, name='index'),
    path('workout', views.workout, name='workout'),
    path('get_workout_type_fields', views.get_workout_type_fields, name='get_workout_type_fields'),
]
