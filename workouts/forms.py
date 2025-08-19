from django import forms

from .models import Workout

class WorkoutForm(forms.ModelForm):
    workout_type = forms.ChoiceField(
        choices=[
            ("Pull Ups", "Pull Ups"),
            ("Deadlifts", "Deadlifts"),
            ("Bulgarian Split Squats", "Bulgarian Split Squats"),
            ("Bench Press", "Bench Press"),
            ("Romainian Deadlifts", "Romainian Deadlifts"),
            ("Boulder", "Boulder"),
            ("Rope Climb", "Rope Climb"),
        ],
    )
    note = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Note'}),
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Workout
        fields = ['workout_type', 'note', 'date']