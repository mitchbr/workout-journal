from datetime import datetime
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import WorkoutForm
from .helpers import getWorkoutsContext
from .models import User, Workout


# Create your views here.
def index(request):
  default_user = User.objects.filter(username="Mitchell").first()
  if not default_user:
    default_user = User.objects.create(username="Mitchell")
    Workout.objects.create(
      user=default_user,
      date=datetime(2025, 6, 21, 10, 30, 0),
      workout_type="Pull Ups",
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
    workout.save()
    
    new_workout_date = workout.date.strftime("%m/%d/%Y")

    context = getWorkoutsContext(request, new_workout_date)
    response = render(request, "workouts.html", context)
    response['HX-Trigger'] = 'workout-added'
    return response
