from django import forms

from .models import Workout, WorkoutType

class WorkoutForm(forms.ModelForm):
    workout_type = forms.ModelChoiceField(queryset=WorkoutType.objects.all(), empty_label="Select a Category")
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