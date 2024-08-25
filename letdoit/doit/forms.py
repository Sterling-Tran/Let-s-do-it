from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['content', 'start_time', 'completion_time', 'cash_amount', 'user_email', 'friend_email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure date fields use 'date' input type
        self.fields['start_time'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['completion_time'].widget = forms.DateInput(attrs={'type': 'date'})

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        completion_time = cleaned_data.get('completion_time')

        # Ensure the completion_time is greater than the start_time
        if completion_time and start_time and completion_time <= start_time:
            raise forms.ValidationError('Completion time must be later than the start time.')

        return cleaned_data