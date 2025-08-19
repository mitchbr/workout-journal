from datetime import datetime, timedelta

from .forms import WorkoutForm
from .models import User, Workout


def getWorkouts(user, view_date):
  dt = datetime.strptime(view_date, "%m/%d/%Y")
  start_date = dt - timedelta(days=dt.weekday())
  end_date = start_date + timedelta(days=6)

  workouts = Workout.objects.filter(user=user, date__range=[start_date,end_date]).order_by("-date")
  workouts_by_date = []
  for workout in workouts:
    if not workouts_by_date or workout.date != workouts_by_date[-1]["date"]:
      workouts_by_date.append({"date": workout.date, "workouts": [workout]})
    elif workouts_by_date[-1]["date"] == workout.date:
      workouts_by_date[-1]["workouts"].append(workout)
  return workouts_by_date

def getWorkoutsContext(request, new_workout_date=None):
  user = User.objects.get(username="Mitchell")
  view_date_str = new_workout_date or request.GET.get('view_date', datetime.today().strftime("%m/%d/%Y"))
  view_date = datetime.strptime(view_date_str, "%m/%d/%Y")
  start_date = view_date - timedelta(days=view_date.weekday())
  next_week = (view_date + timedelta(days=7)).strftime("%m/%d/%Y")
  prev_week = (view_date - timedelta(days=7)).strftime("%m/%d/%Y")
  workouts = getWorkouts(user, view_date_str)
  
  return {
    "user": user, 
    "workouts": workouts, 
    "form": WorkoutForm(),
    "next_week": next_week,
    "prev_week": prev_week,
    "start_date": start_date
  }