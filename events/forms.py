from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    """ Form for adding and editing events """
    class Meta:
        model = Event
        fields = ('title', 'description', 'start_date',
                  'end_date', 'start_time', 'end_time', 'location',)
        readonly_fields = ('creator', 'created_on', 'slug',)
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter event title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter event description'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter event location'}),
            'start_date': forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}),
            'end_date': forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}),
            'start_time': forms.TimeInput(attrs={'placeholder': 'hh:mm'}),
            'end_time': forms.TimeInput(attrs={'placeholder': 'hh:mm'}),
        }
