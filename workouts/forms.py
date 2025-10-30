from django import forms

from .models import Workout, WorkoutType

class WorkoutForm(forms.ModelForm):
    workout_type = forms.ModelChoiceField(queryset=WorkoutType.objects.all().order_by("title"), empty_label="Select a Category")
    note = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Note', 'class': 'text-base'}),
        required=False
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'text-base'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Workout
        fields = ['workout_type', 'note', 'date']
        
class WorkoutUpdateForm(forms.ModelForm):
    note = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Note', 'class': 'text-base'}),
        required=False
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'text-base'}),
        input_formats=['%Y-%m-%d']
    )
    
    class Meta:
        model = Workout
        fields = ['date', 'note']