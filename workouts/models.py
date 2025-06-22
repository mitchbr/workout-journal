from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    workout_type = models.CharField(max_length=255)
    note = models.TextField(blank=True, null=True)
    data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"
