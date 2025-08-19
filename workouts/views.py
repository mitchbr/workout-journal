from datetime import datetime, timedelta
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import WorkoutForm
from .helpers import getWorkouts
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

  user = User.objects.get(username="Mitchell")
  view_date_str = request.GET.get('view_date', datetime.today().strftime("%m/%d/%Y"))
  view_date = datetime.strptime(view_date_str, "%m/%d/%Y")
  start_date = view_date - timedelta(days=view_date.weekday())
  next_week = (view_date + timedelta(days=7)).strftime("%m/%d/%Y")
  prev_week = (view_date - timedelta(days=7)).strftime("%m/%d/%Y")
  workouts = getWorkouts(user, view_date_str)

  context = {
    "user": user, 
    "workouts": workouts, 
    "form": WorkoutForm(),
    "next_week": next_week,
    "prev_week": prev_week,
    "start_date": start_date
  }
  return render(request, "workouts.html", context)

@require_http_methods(["POST"])
def workout(request):
  form = WorkoutForm(request.POST)
  if form.is_valid():
    workout = form.save(commit=False)
    user = User.objects.get(username="Mitchell")
    workout.user = user
    workout.save()

    view_date = request.GET.get('view_date', datetime.today().strftime("%m/%d/%Y"))
    workouts = getWorkouts(user, view_date)
    context = {"workouts": workouts}
    response = render(request, "partials/workouts_list.html", context)
    response['HX-Trigger'] = 'workout-added'
    return response
