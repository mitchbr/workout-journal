from django.shortcuts import render

from .models import User, Workout


# Create your views here.
def index(request):
    user = User.objects.get(username="Mitchell")
    workouts = Workout.objects.filter(user=user).order_by("-date")
    # User.objects.create(username="Mitchell")
    # Workout.objects.create(user=u, date=datetime(2025, 6, 21, 10, 30, 0), workout_type="Pull Ups", data={"weight": 0, "reps": 8}, note="Shoulder sore")
    context = {"test": "hi!", "user": user, "workouts": workouts}
    return render(request, "workouts.html", context)
