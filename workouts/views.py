from datetime import datetime
from django.shortcuts import render

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
    workouts = getWorkouts(user)
    context = {"user": user, "workouts": workouts}
    return render(request, "workouts.html", context)
