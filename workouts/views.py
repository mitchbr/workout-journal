from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import WorkoutForm
from .helpers import getWorkoutsContext
from .models import User, Workout, WorkoutType

# Create your views here.
def index(request):
  default_user = User.objects.filter(username="Mitchell").first()
  if not default_user:
    default_user = User.objects.create(username="Mitchell")
    WorkoutType.objects.create(title="Deadlift", fields={"weight": "number", "reps": "number"})
    WorkoutType.objects.create(title="Beanch Press", fields={"weight": "number", "reps": "number"})
    WorkoutType.objects.create(title="Bulgarian Split Squats", fields={"weight": "number", "reps": "number"})
    WorkoutType.objects.create(title="Romanian Deadlift", fields={"weight": "number", "reps": "number"})
    WorkoutType.objects.create(title="Barbell Row", fields={"weight": "number", "reps": "number"})
    WorkoutType.objects.create(title="Shoulder Press", fields={"weight": "number", "reps": "number"})
    WorkoutType.objects.create(title="Single Leg RDL", fields={"weight": "number", "reps": "number"})
    WorkoutType.objects.create(title="Hangboard", fields={"weight": "number", "reps": "number"})
    WorkoutType.objects.create(title="Dumbbell Row", fields={"weight": "number", "reps": "number"})
    WorkoutType.objects.create(title="Bouldering", fields={"location": "text"})
    WorkoutType.objects.create(title="Rope Climbing", fields={"location": "text"})
    WorkoutType.objects.create(title="Other", fields={"exercise": "text"})
    workout_type = WorkoutType.objects.create(title="Pull Ups", fields={"weight": "number", "reps": "number"})
    Workout.objects.create(
      user=default_user,
      date=datetime(2025, 6, 21, 10, 30, 0),
      workout_type=workout_type,
      data={"weight": 0, "reps": 8},
      note="Shoulder sore",
    )

  context = getWorkoutsContext(request)
  return render(request, "workouts.html", context)

@require_http_methods(["POST"])
def workout(request):
  form = WorkoutForm(request.POST)
  if form.is_valid():
    workout = form.save(commit=False)
    user = User.objects.get(username="Mitchell")
    workout.user = user

    dynamic_items = {k.removeprefix('dynamic_'): v for k, v in request.POST.items() if k.startswith('dynamic_')}
    workout.data = dynamic_items

    workout.save()
  
    new_workout_date = workout.date.strftime("%m/%d/%Y")

    context = getWorkoutsContext(request, new_workout_date)
    response = render(request, "workouts.html", context)
    response['HX-Trigger'] = 'workout-added'
    return response

@require_http_methods(["GET"])
def get_workout_type_fields(request):
  workout_type_ids = request.GET.get('workout_type')
  
  if not workout_type_ids:
    return HttpResponse('')
  
  try:
    workout_type = WorkoutType.objects.get(id=workout_type_ids)
    fields = workout_type.fields or []
    processed_fields = []
    for field in fields:
      processed_fields.append({'title': field, 'datatype': fields[field]})
    return render(request, 'partials/workout_type_field.html', {
        'fields': processed_fields
    })
  except (WorkoutType.DoesNotExist, ValueError):
    return HttpResponse('')
