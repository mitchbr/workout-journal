from .models import Workout


def getWorkouts(user):
    workouts = Workout.objects.filter(user=user).order_by("-date")
    workouts_by_date = []
    for workout in workouts:
        if not workouts_by_date or workout.date != workouts_by_date[-1]["date"]:
            workouts_by_date.append({"date": workout.date, "workouts": [workout]})
        elif workouts_by_date[-1]["date"] == workout.date:
            workouts_by_date[-1]["workouts"].append(workout)
    return workouts_by_date
