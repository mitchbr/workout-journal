from datetime import datetime, timedelta

from .models import Workout


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
