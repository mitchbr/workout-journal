from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class WorkoutType(models.Model):
    title = models.CharField(max_length=255)
    fields = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.title

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    workout_type = models.ForeignKey(WorkoutType, on_delete=models.PROTECT)
    note = models.TextField(blank=True, null=True)
    data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"
