from django import forms

from .models import Habit, Record, Observer


class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('title', 'action', 'goal', 'units',)


class RecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ('habit', 'date', 'achievement',)
        widgets = {
            'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'type': 'date'})
        }
