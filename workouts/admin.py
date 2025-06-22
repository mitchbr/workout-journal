from django.contrib import admin

from workouts.models import User, Workout

# Register your models here.
admin.site.register(User)
admin.site.register(Workout)
