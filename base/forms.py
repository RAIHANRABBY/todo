from datetime import date, datetime
from django import forms
from .models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'description','date']
        widgets={
            'title':forms.TextInput(attrs={'placeholder': 'Title'}),
            'date':forms.DateInput(attrs={'type':'date','min':date.today}),
        }
